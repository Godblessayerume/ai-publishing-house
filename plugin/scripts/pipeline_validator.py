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
    1:  "novel-genre-picker",
    2:  "novel-story-seed-writer",
    3:  "novel-3-act-outliner",
    4:  "build-the-world",
    5:  "outline-architect",
    6:  "book-title-generator",
    7:  "novel-chapter-mapper",
    8:  "novel-chapter-drafter",
    9:  "novel-editor",
    10: "novel-copyeditor",
    11: "novel-publisher",
    12: "novel-proofreader",
    13: "book-cover-prompt-generator",
    14: "amazon-upload-kit",
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

_ARTICLES = {"the", "a", "an", "of", "in", "at", "on", "into", "near", "by"}


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def fail(step, reason):
    return {"step": step, "skill": PIPELINE_STEPS.get(step, "?"), "ok": False, "reason": reason}


def ok(step, note=""):
    return {"step": step, "skill": PIPELINE_STEPS.get(step, "?"), "ok": True, "note": note}


# ── Steps 1–6: pre-draft checks ──────────────────────────────────────────────

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


# ── Shared helpers ────────────────────────────────────────────────────────────

def find_chapter_map(search_dir):
    candidates = glob.glob(os.path.join(search_dir, "*-chapter-map.md"))
    return candidates[0] if candidates else None


def count_chapter_entries(chapter_map_path):
    content = read_text(chapter_map_path)
    matches = re.findall(r"^###?\s+Chapter\s+\d+", content, re.MULTILINE | re.IGNORECASE)
    return len(matches)


def sanitize_folder_name(title):
    result = title.replace(":", " -")
    for ch in '<>"/\\|?*':
        result = result.replace(ch, "")
    result = re.sub(r"\s{2,}", " ", result)
    return result.strip()


def get_title_folder(book_dir):
    path = os.path.join(book_dir, "book-title.md")
    if not os.path.exists(path):
        return None
    content = read_text(path)
    m = re.search(r"final\s+title\s*[:\-]\s*(.+)", content, re.IGNORECASE)
    if not m:
        return None
    title = m.group(1).strip().strip("*").strip()
    return os.path.join(book_dir, sanitize_folder_name(title)) if title else None


def parse_chapter_map(map_path):
    """Return [{num, setting}] for each chapter entry in the map."""
    content = read_text(map_path)
    chapters = []
    blocks = re.split(r"(?=^#{2,3}\s+Chapter\s+\d+)", content, flags=re.MULTILINE | re.IGNORECASE)
    for block in blocks:
        num_match = re.search(r"Chapter\s+(\d+)", block, re.IGNORECASE)
        if not num_match:
            continue
        setting_match = re.search(r"\*\*Setting:\*\*\s*(.+)", block)
        chapters.append({
            "num": int(num_match.group(1)),
            "setting": setting_match.group(1).strip() if setting_match else None,
        })
    return sorted(chapters, key=lambda c: c["num"])


def setting_search_term(setting_str):
    words = [w.rstrip(".,;") for w in setting_str.split()]
    content_words = [w for w in words if w.lower() not in _ARTICLES]
    return " ".join(content_words[:2]) if content_words else (words[0] if words else "")


# ── Steps 7–14: draft + post-draft checks ─────────────────────────────────────

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
        return fail(8, f"Only {actual}/{expected} chapters drafted. Resume from chapter-{actual + 1:02d}.md")

    # Map compliance: verify each chapter mentions its assigned setting
    map_chapters = parse_chapter_map(map_path)
    drift = []
    for entry in map_chapters:
        if not entry["setting"]:
            continue
        chapter_file = os.path.join(chapters_dir, f"chapter-{entry['num']:02d}.md")
        if not os.path.exists(chapter_file):
            continue
        term = setting_search_term(entry["setting"])
        if term and not re.search(re.escape(term), read_text(chapter_file), re.IGNORECASE):
            drift.append(f"ch{entry['num']:02d} (map: {entry['setting']!r})")

    if drift:
        summary = ", ".join(drift[:4]) + (f" (+{len(drift) - 4} more)" if len(drift) > 4 else "")
        return ok(8, f"all {actual} chapters drafted — setting drift in {len(drift)} chapter(s): {summary}")

    return ok(8, f"all {actual} chapters drafted, all settings present")


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
    unedited = [f for f in chapter_files if os.path.getmtime(os.path.join(chapters_dir, f)) <= map_mtime]
    if unedited:
        return fail(9, f"{len(unedited)} chapters appear unedited (mtime predates chapter-map). First: {unedited[0]}")
    return ok(9, f"all {len(chapter_files)} chapters edited")


def check_step_10(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(10, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "copyedit-report.md")
    if not os.path.exists(path):
        return fail(10, f"copyedit-report.md is missing from title folder '{os.path.basename(title_dir)}'")
    if os.path.getsize(path) < 20:
        return fail(10, "copyedit-report.md is empty")
    return ok(10, "copyedit report present")


def check_step_11(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(11, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "manuscript-final.md")
    if not os.path.exists(path):
        alt = os.path.join(title_dir, "manuscript_final.md")
        if os.path.exists(alt):
            path = alt
        else:
            return fail(11, f"manuscript-final.md is missing from title folder '{os.path.basename(title_dir)}'")
    chapters_dir = os.path.join(title_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        return ok(11, f"manuscript exists ({os.path.getsize(path)} bytes), no chapters/ folder to compare")
    chapter_files = [f for f in os.listdir(chapters_dir) if re.match(r"chapter-\d+\.md$", f)]
    chapter_total = sum(os.path.getsize(os.path.join(chapters_dir, f)) for f in chapter_files)
    manuscript_size = os.path.getsize(path)
    if manuscript_size < chapter_total * 0.8:
        return fail(11, f"manuscript ({manuscript_size} bytes) is less than 80% of chapter total ({chapter_total} bytes) — compilation may be incomplete")
    return ok(11, f"manuscript {manuscript_size} bytes, chapters total {chapter_total} bytes")


def check_step_12(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(12, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "proofread-report.md")
    if not os.path.exists(path):
        return fail(12, f"proofread-report.md is missing from title folder '{os.path.basename(title_dir)}'")
    if os.path.getsize(path) < 20:
        return fail(12, "proofread-report.md is empty")
    return ok(12, "proofread report present")


def check_step_13(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(13, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "book-cover-prompt.md")
    if not os.path.exists(path):
        return fail(13, f"book-cover-prompt.md is missing from title folder '{os.path.basename(title_dir)}'")
    if os.path.getsize(path) < 50:
        return fail(13, "book-cover-prompt.md is too small (under 50 bytes)")
    return ok(13, "cover prompt present")


def check_step_14(book_dir):
    title_dir = get_title_folder(book_dir)
    if not title_dir:
        return fail(14, "Cannot determine title folder — book-title.md missing (Step 6 incomplete)")
    path = os.path.join(title_dir, "amazon-upload-kit.md")
    if not os.path.exists(path):
        return fail(14, f"amazon-upload-kit.md is missing from title folder '{os.path.basename(title_dir)}'")
    content = read_text(path)
    missing_sections = []
    if not re.search(r"##\s+Description", content, re.IGNORECASE):
        missing_sections.append("Description")
    if not re.search(r"##\s+Keywords", content, re.IGNORECASE):
        missing_sections.append("Keywords")
    if not re.search(r"##\s+(?:Recommended\s+)?Categories", content, re.IGNORECASE):
        missing_sections.append("Categories")
    if missing_sections:
        return fail(14, f"amazon-upload-kit.md missing sections: {', '.join(missing_sections)}")
    return ok(14, "upload kit complete (description, keywords, categories present)")


# ── Registry and runner ───────────────────────────────────────────────────────

STEP_CHECKS = {
    1:  check_step_1,
    2:  check_step_2,
    3:  check_step_3,
    4:  check_step_4,
    5:  check_step_5,
    6:  check_step_6,
    7:  check_step_7,
    8:  check_step_8,
    9:  check_step_9,
    10: check_step_10,
    11: check_step_11,
    12: check_step_12,
    13: check_step_13,
    14: check_step_14,
}


def validate_step(book_dir, step):
    if step not in STEP_CHECKS:
        return {"step": step, "ok": False, "reason": f"Unknown step number: {step}"}
    return STEP_CHECKS[step](book_dir)


def determine_next_step(book_dir):
    for step in range(1, 15):
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
    parser.add_argument("--step", type=int, help="Validate a specific step (1-14).")
    parser.add_argument("--all", action="store_true", help="Validate all steps and report status.")
    parser.add_argument("--check-state", action="store_true", help="Print the next pending step number (or 'complete').")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of formatted text.")

    args = parser.parse_args()

    if not os.path.isdir(args.book_dir):
        print(f"Error: book directory '{args.book_dir}' does not exist.", file=sys.stderr)
        sys.exit(2)

    if args.check_state:
        next_step = determine_next_step(args.book_dir)
        if next_step is None:
            print(json.dumps({"next_step": None, "status": "complete"}) if args.json else "complete")
            sys.exit(0)
        if args.json:
            print(json.dumps({"next_step": next_step, "skill": PIPELINE_STEPS[next_step]}))
        else:
            print(f"{next_step} ({PIPELINE_STEPS[next_step]})")
        sys.exit(0)

    if args.all:
        results = [validate_step(args.book_dir, s) for s in range(1, 15)]
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print("=" * 60)
            print("    PIPELINE VALIDATION REPORT")
            print(f"    Book: {args.book_dir}")
            print("=" * 60)
            for r in results:
                print_result(r, formatted=True)
        sys.exit(1 if any(not r["ok"] for r in results) else 0)

    if args.step:
        result = validate_step(args.book_dir, args.step)
        print_result(result, formatted=not args.json)
        sys.exit(0 if result["ok"] else 1)

    parser.print_help()
    sys.exit(2)


if __name__ == "__main__":
    main()
