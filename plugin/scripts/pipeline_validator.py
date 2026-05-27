#!/usr/bin/env python3
"""
Pipeline Validator for AI Publishing House.
Checks output completeness for each step of the novel-creation pipeline.

Used by the orchestrator skill between auto-chained steps to ensure each
handoff is well-formed before invoking the next skill. Also supports a
--check-state mode that returns the next step number for a given book folder.
"""

import argparse
import sys
import re
import json
import os
import glob

PIPELINE_STEPS = {
    1: "novel-genre-picker",
    2: "novel-story-seed-writer",
    3: "novel-3-act-outliner",
    4: "build-the-world",
    5: "outline-architect",
    6: "book-title-generator",
    7: "novel-chapter-mapper",
    8: "novel-chapter-drafter",
    9: "novel-editor",
    10: "novel-publisher",
    11: "book-cover-prompt-generator",
}

CWDAC_MARKERS = ["(C)", "(W)", "(D)", "(A)"]

BEAT_HEADINGS = [
    "Exposition",
    "Inciting Incident",
    "Plot Point 1",
    "Rising Action",
    "Midpoint",
    "Plot Point 2",
    "Pre-Climax",
    "Climax",
    "Denouement",
]


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def fail(step, reason):
    return {"step": step, "skill": PIPELINE_STEPS.get(step, "?"), "ok": False, "reason": reason}


def ok(step, note=""):
    return {"step": step, "skill": PIPELINE_STEPS.get(step, "?"), "ok": True, "note": note}


def check_step_1(book_dir):
    path = os.path.join(book_dir, "story-config.md")
    if not os.path.exists(path):
        return fail(1, "story-config.md is missing")
    content = read_text(path)
    if not re.search(r"sub[\s-]?genre", content, re.IGNORECASE):
        return fail(1, "story-config.md missing 'Sub-Genre' field")
    archetype_refs = re.findall(r"#\d+\s*[—\-]", content)
    if len(archetype_refs) < 2:
        return fail(1, f"story-config.md references {len(archetype_refs)} archetypes (need at least 2 in '#N — Name' form)")
    return ok(1, f"sub-genre present, {len(archetype_refs)} archetype references found")


def check_step_2(book_dir):
    path = os.path.join(book_dir, "story-seed.md")
    if not os.path.exists(path):
        return fail(2, "story-seed.md is missing")
    content = read_text(path)
    missing = [m for m in CWDAC_MARKERS if m not in content]
    if missing:
        return fail(2, f"story-seed.md missing C/W/D/A/C markers: {', '.join(missing)}")
    return ok(2, "C/W/D/A/C breakdown present")


def check_step_3(book_dir):
    path = os.path.join(book_dir, "3-act-outline.md")
    if not os.path.exists(path):
        return fail(3, "3-act-outline.md is missing")
    content = read_text(path)
    found = [b for b in BEAT_HEADINGS if re.search(rf"\b{re.escape(b)}\b", content, re.IGNORECASE)]
    if len(found) < 9:
        missing = [b for b in BEAT_HEADINGS if b not in found]
        return fail(3, f"3-act-outline.md missing beats: {', '.join(missing)}")
    return ok(3, "all 9 beats present")


def check_step_4(book_dir):
    world_map = os.path.join(book_dir, "world", "world-map.md")
    if not os.path.exists(world_map):
        return fail(4, "world/world-map.md is missing")
    settings_dir = os.path.join(book_dir, "world", "settings")
    if not os.path.isdir(settings_dir):
        return fail(4, "world/settings/ directory is missing")
    setting_files = [f for f in os.listdir(settings_dir) if f.endswith(".md")]
    if len(setting_files) < 3:
        return fail(4, f"world/settings/ has {len(setting_files)} files (need at least 3)")
    bios_dir = os.path.join(book_dir, "world", "characters", "bios")
    if not os.path.isdir(bios_dir):
        return fail(4, "world/characters/bios/ directory is missing")
    bio_files = [f for f in os.listdir(bios_dir) if f.endswith(".md")]
    if len(bio_files) < 3:
        return fail(4, f"world/characters/bios/ has {len(bio_files)} files (need at least 3)")
    return ok(4, f"{len(setting_files)} settings, {len(bio_files)} character bios")


def check_step_5(book_dir):
    path = os.path.join(book_dir, "3-act-outline.md")
    if not os.path.exists(path):
        return fail(5, "3-act-outline.md is missing (Step 3 incomplete)")
    content = read_text(path)
    if not re.search(r"^##\s+Macro Architecture", content, re.MULTILINE | re.IGNORECASE):
        return fail(5, "3-act-outline.md missing '## Macro Architecture' section (outline-architect did not upgrade)")
    return ok(5, "Macro Architecture section present")


def check_step_6(book_dir):
    path = os.path.join(book_dir, "book-title.md")
    if not os.path.exists(path):
        return fail(6, "book-title.md is missing")
    content = read_text(path)
    if not re.search(r"final\s+title", content, re.IGNORECASE):
        return fail(6, "book-title.md missing 'Final Title:' line")
    return ok(6, "final title locked")


def find_chapter_map(search_dir):
    candidates = glob.glob(os.path.join(search_dir, "*-chapter-map.md"))
    if not candidates:
        return None
    return candidates[0]


def count_chapter_entries(chapter_map_path):
    content = read_text(chapter_map_path)
    matches = re.findall(r"^###?\s+Chapter\s+\d+", content, re.MULTILINE | re.IGNORECASE)
    return len(matches)


def sanitize_folder_name(title):
    """Sanitize a book title for use as a Windows folder name."""
    result = title.replace(':', ' -')
    for ch in '<>"/\\|?*':
        result = result.replace(ch, '')
    result = re.sub(r'\s{2,}', ' ', result)
    return result.strip()


def get_title_folder(book_dir):
    """Return path to the title subfolder derived from book-title.md at the book root."""
    path = os.path.join(book_dir, "book-title.md")
    if not os.path.exists(path):
        return None
    content = read_text(path)
    m = re.search(r'final\s+title\s*[:\-]\s*(.+)', content, re.IGNORECASE)
    if not m:
        return None
    title = m.group(1).strip().strip('*').strip()
    if not title:
        return None
    return os.path.join(book_dir, sanitize_folder_name(title))


def check_step_7(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(7, "Cannot determine title folder — book-title.md missing or has no 'Final Title:' line (Step 6 incomplete)")
    path = find_chapter_map(title_dir)
    if not path:
        return fail(7, f"No '*-chapter-map.md' found in title folder '{os.path.basename(title_dir)}'")
    count = count_chapter_entries(path)
    if count < 10:
        return fail(7, f"chapter-map has {count} chapter entries (expected at least 10)")
    return ok(7, f"{count} chapters mapped")


def check_step_8(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(8, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    chapters_dir = os.path.join(title_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        return fail(8, f"chapters/ directory is missing inside title folder '{os.path.basename(title_dir)}'")
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if re.match(r"chapter-\d+\.md$", f)])
    if not chapter_files:
        return fail(8, "chapters/ directory is empty")
    map_path = find_chapter_map(title_dir)
    if not map_path:
        return fail(8, "No chapter map found in title folder — cannot verify completeness")
    expected = count_chapter_entries(map_path)
    actual = len(chapter_files)
    if actual < expected:
        next_chapter = actual + 1
        return fail(
            8,
            f"Only {actual}/{expected} chapters drafted. Resume from chapter-{next_chapter:02d}.md",
        )
    return ok(8, f"all {actual} chapters drafted")


def check_step_9(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(9, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    chapters_dir = os.path.join(title_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        return fail(9, f"chapters/ directory is missing inside title folder '{os.path.basename(title_dir)}'")
    map_path = find_chapter_map(title_dir)
    if not map_path:
        return fail(9, "No chapter map found in title folder — cannot establish baseline")
    map_mtime = os.path.getmtime(map_path)
    chapter_files = sorted([f for f in os.listdir(chapters_dir) if re.match(r"chapter-\d+\.md$", f)])
    if not chapter_files:
        return fail(9, "chapters/ directory has no chapter files")
    unedited = []
    for f in chapter_files:
        full = os.path.join(chapters_dir, f)
        if os.path.getmtime(full) <= map_mtime:
            unedited.append(f)
    if unedited:
        return fail(9, f"{len(unedited)} chapters appear unedited (mtime predates chapter-map). First: {unedited[0]}")
    return ok(9, f"all {len(chapter_files)} chapters edited (mtime post-dates chapter-map)")


def check_step_10(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(10, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "manuscript-final.md")
    if not os.path.exists(path):
        alt = os.path.join(title_dir, "manuscript_final.md")
        if os.path.exists(alt):
            path = alt
        else:
            return fail(10, f"manuscript-final.md is missing from title folder '{os.path.basename(title_dir)}'")
    chapters_dir = os.path.join(title_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        return ok(10, f"manuscript exists ({os.path.getsize(path)} bytes), no chapters/ folder to compare")
    chapter_files = [f for f in os.listdir(chapters_dir) if re.match(r"chapter-\d+\.md$", f)]
    chapter_total = sum(os.path.getsize(os.path.join(chapters_dir, f)) for f in chapter_files)
    manuscript_size = os.path.getsize(path)
    if manuscript_size < chapter_total * 0.8:
        return fail(
            10,
            f"manuscript size ({manuscript_size} bytes) is less than 80% of chapter total ({chapter_total} bytes) — compilation may be incomplete",
        )
    return ok(10, f"manuscript {manuscript_size} bytes, chapters total {chapter_total} bytes")


def check_step_11(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(11, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "book-cover-prompt.md")
    if not os.path.exists(path):
        return fail(11, f"book-cover-prompt.md is missing from title folder '{os.path.basename(title_dir)}'")
    if os.path.getsize(path) < 50:
        return fail(11, "book-cover-prompt.md is too small (under 50 bytes)")
    return ok(11, "cover prompt present")


STEP_CHECKS = {
    1: check_step_1,
    2: check_step_2,
    3: check_step_3,
    4: check_step_4,
    5: check_step_5,
    6: check_step_6,
    7: check_step_7,
    8: check_step_8,
    9: check_step_9,
    10: check_step_10,
    11: check_step_11,
}


def validate_step(book_dir, step):
    if step not in STEP_CHECKS:
        return {"step": step, "ok": False, "reason": f"Unknown step number: {step}"}
    return STEP_CHECKS[step](book_dir)


def determine_next_step(book_dir):
    for step in range(1, 12):
        result = validate_step(book_dir, step)
        if not result["ok"]:
            return step
    return None


def print_result(result, formatted=True):
    if not formatted:
        print(json.dumps(result, indent=2))
        return
    if result["ok"]:
        print(f"[OK]   Step {result['step']} ({result['skill']}): {result.get('note', 'valid')}")
    else:
        print(f"[FAIL] Step {result['step']} ({result['skill']}): {result['reason']}")


def main():
    parser = argparse.ArgumentParser(description="Pipeline Validator for AI Publishing House.")
    parser.add_argument("--book-dir", required=True, help="Path to the book folder inside the Fiction Library vault.")
    parser.add_argument("--step", type=int, help="Validate a specific step (1-11).")
    parser.add_argument("--all", action="store_true", help="Validate all steps and report status.")
    parser.add_argument("--check-state", action="store_true", help="Print the next pending step number (or 'complete'). Useful for the orchestrator.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of formatted text.")

    args = parser.parse_args()

    if not os.path.isdir(args.book_dir):
        print(f"Error: book directory '{args.book_dir}' does not exist.", file=sys.stderr)
        sys.exit(2)

    if args.check_state:
        next_step = determine_next_step(args.book_dir)
        if next_step is None:
            if args.json:
                print(json.dumps({"next_step": None, "status": "complete"}))
            else:
                print("complete")
            sys.exit(0)
        if args.json:
            print(json.dumps({"next_step": next_step, "skill": PIPELINE_STEPS[next_step]}))
        else:
            print(f"{next_step} ({PIPELINE_STEPS[next_step]})")
        sys.exit(0)

    if args.all:
        results = [validate_step(args.book_dir, s) for s in range(1, 12)]
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("=" * 60)
            print("    PIPELINE VALIDATION REPORT")
            print(f"    Book: {args.book_dir}")
            print("=" * 60)
            for r in results:
                print_result(r, formatted=True)
        any_fail = any(not r["ok"] for r in results)
        sys.exit(1 if any_fail else 0)

    if args.step:
        result = validate_step(args.book_dir, args.step)
        print_result(result, formatted=not args.json)
        sys.exit(0 if result["ok"] else 1)

    parser.print_help()
    sys.exit(2)


if __name__ == "__main__":
    main()
