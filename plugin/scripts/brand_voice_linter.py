#!/usr/bin/env python3
"""
Brand Voice Linter for AI Publishing House.
Checks draft chapter files against the Godbless Ayerume Author Brand Voice Guide.

Rule #1  — Single-sentence opener: first paragraph must be exactly one sentence.
Rule #14 — Pronoun opener: paragraph begins with she/he/they before naming the character.
Rule #14 — Pronoun run: 3+ consecutive sentences starting with the same subject pronoun.
"""

import argparse
import sys
import re
import json
import os

SUBJECT_PRONOUNS = {"she", "he", "they"}


def analyze_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    content = content.replace("\r\n", "\n")

    # Strip YAML frontmatter while preserving line numbers
    text_content = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter_lines = parts[1].count("\n") + 2
            text_content = "\n" * frontmatter_lines + parts[2]

    lines = text_content.split("\n")
    issues = []

    # Rule #1 — single-sentence opener
    first_p = None
    first_p_line = 0
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and stripped != "---":
            first_p = stripped
            first_p_line = idx + 1
            break

    if first_p:
        sentences = re.split(r'(?<=[.!?])\s+', first_p)
        if len(sentences) > 1:
            issues.append({
                "type": "blocky_opener",
                "severity": "WARNING",
                "line": first_p_line,
                "message": (
                    f"First paragraph has {len(sentences)} sentences. "
                    "Rule #1 requires a single-sentence opener — one sentence that establishes "
                    "Who, Where, and Genre/Mood before anything else."
                ),
                "context": first_p[:120] + "..." if len(first_p) > 120 else first_p
            })

    # Rule #14 — per-paragraph pronoun checks
    current_paragraph = []
    paragraph_start_line = 0

    for idx, line in enumerate(lines):
        line_num = idx + 1
        stripped = line.strip()

        if stripped.startswith("#") or stripped == "---":
            continue

        if stripped:
            if not current_paragraph:
                paragraph_start_line = line_num
            current_paragraph.append(stripped)
        else:
            if current_paragraph:
                p_text = " ".join(current_paragraph)
                analyze_paragraph(p_text, paragraph_start_line, issues)
                current_paragraph = []

    if current_paragraph:
        p_text = " ".join(current_paragraph)
        analyze_paragraph(p_text, paragraph_start_line, issues)

    return issues


def first_word(sentence):
    m = re.match(r'\b(\w+)', sentence.strip())
    return m.group(1).lower() if m else ""


def analyze_paragraph(p_text, start_line, issues):
    sentences = re.split(r'(?<=[.!?])\s+', p_text)
    if not sentences:
        return

    # Rule #14a — pronoun opener
    # If the paragraph's first sentence starts with she/he/they, the character
    # hasn't been named yet in this paragraph — reader must guess who is on stage.
    opener = first_word(sentences[0])
    if opener in SUBJECT_PRONOUNS:
        issues.append({
            "type": "pronoun_opener",
            "severity": "WARNING",
            "line": start_line,
            "message": (
                f"Paragraph opens with '{opener.capitalize()}' before naming the character (Rule #14). "
                "Use the character's name in the first sentence so the reader knows immediately who is on stage."
            ),
            "context": p_text[:120] + "..." if len(p_text) > 120 else p_text
        })

    # Rule #14b — pronoun run
    # Three or more consecutive sentences beginning with the same subject pronoun
    # creates the distance the rule is designed to prevent.
    if len(sentences) >= 3:
        run_pronoun = None
        run_start = 0
        run_count = 0
        reported_at = -1

        for i, sent in enumerate(sentences):
            w = first_word(sent)
            if w in SUBJECT_PRONOUNS:
                if w == run_pronoun:
                    run_count += 1
                else:
                    run_pronoun = w
                    run_start = i
                    run_count = 1
            else:
                run_pronoun = None
                run_count = 0

            if run_count >= 3 and run_start != reported_at:
                reported_at = run_start
                excerpt = " ".join(sentences[run_start:run_start + run_count])
                issues.append({
                    "type": "pronoun_run",
                    "severity": "INFO",
                    "line": start_line,
                    "message": (
                        f"{run_count} consecutive sentences begin with "
                        f"'{run_pronoun.capitalize()}' (Rule #14). "
                        "Insert the character's name to re-anchor the reader."
                    ),
                    "context": excerpt[:120] + "..." if len(excerpt) > 120 else excerpt
                })


def main():
    parser = argparse.ArgumentParser(description="Brand Voice Linter for AI Publishing House.")
    parser.add_argument("file", help="Path to the draft chapter markdown file.")
    parser.add_argument("--output", help="Write the report to this path as JSON.")
    parser.add_argument("--json", action="store_true", help="Print the report to stdout as JSON.")

    args = parser.parse_args()
    issues = analyze_file(args.file)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(issues, f, indent=2)
            print(f"Report written to '{args.output}'")
        except Exception as e:
            print(f"Error writing output: {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.json:
        print(json.dumps(issues, indent=2))
        return

    if not issues:
        print("Compliant. No Brand Voice violations found.")
        return

    print("=" * 60)
    print("      BRAND VOICE LINT REPORT - AI PUBLISHING HOUSE")
    print("=" * 60)

    warnings = [i for i in issues if i["severity"] == "WARNING"]
    infos = [i for i in issues if i["severity"] == "INFO"]
    print(f"Found {len(issues)} issues ({len(warnings)} Warnings, {len(infos)} Suggestions):\n")

    for issue in issues:
        tag = "[WARNING]" if issue["severity"] == "WARNING" else "[INFO]   "
        line_info = f"Line {issue['line']}: " if issue.get("line") else ""
        print(f"{tag} {line_info}{issue['message']}")
        print(f"  Context: \"{issue['context']}\"")
        print("-" * 60)


if __name__ == "__main__":
    main()
