#!/usr/bin/env python3
"""
Brand Voice Linter for AI Publishing House.
Analyzes draft manuscript files for compliance with the Godbless Ayerume Author Brand Voice Guide.
- Checks for single-sentence openers in the first paragraph.
- Checks for blocky paragraphs (> 4 sentences).
- Checks for high pronoun density.
"""

import argparse
import sys
import re
import json
import os

# Pronoun set for checking pronoun density
PRONOUNS = {
    "he", "she", "they", "him", "her", "them", "his", "hers", "their", "theirs",
    "himself", "herself", "themselves", "she'd", "he'd", "they'd", "she's", "he's", "they're"
}

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

    # Normalize line endings
    content = content.replace("\r\n", "\n")

    # Strip YAML frontmatter if present, but maintain line padding
    original_lines = content.split("\n")
    text_content = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter_lines = parts[1].count("\n") + 2
            text_content = "\n" * frontmatter_lines + parts[2]

    lines = text_content.split("\n")
    issues = []

    # 1. Single-Sentence Opener & Grounding
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
                "message": f"First paragraph has {len(sentences)} sentences. The Brand Voice Guide strictly requires a single-sentence opener to start a chapter or section.",
                "context": first_p
            })

    # 2. Blocky Paragraphs (> 4 sentences) & High Pronoun Density
    current_paragraph = []
    paragraph_start_line = 0

    for idx, line in enumerate(lines):
        line_num = idx + 1
        stripped = line.strip()

        # If it's a heading or frontmatter tag, skip
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

    # Analyze trailing paragraph if any
    if current_paragraph:
        p_text = " ".join(current_paragraph)
        analyze_paragraph(p_text, paragraph_start_line, issues)

    return issues

def analyze_paragraph(p_text, start_line, issues):
    # Split into sentences (simple boundary check)
    sentences = re.split(r'(?<=[.!?])\s+', p_text)
    
    # Rule 1: Paragraphs shouldn't be blocky (>4 sentences)
    if len(sentences) > 4:
        issues.append({
            "type": "blocky_paragraph",
            "severity": "WARNING",
            "line": start_line,
            "message": f"Paragraph contains {len(sentences)} sentences (limit: 4). Break it up to maintain a fast, staccato/legato reading rhythm.",
            "context": p_text[:80] + "..." if len(p_text) > 80 else p_text
        })

    # Rule 2: Pronoun Density
    words = re.findall(r"\b\w+['-]?\w*\b", p_text.lower())
    total_words = len(words)
    if total_words > 15:  # Only check meaningful paragraphs
        pronoun_count = sum(1 for w in words if w in PRONOUNS)
        ratio = pronoun_count / total_words
        if ratio > 0.15:  # Over 15% pronouns
            issues.append({
                "type": "pronoun_density",
                "severity": "INFO",
                "line": start_line,
                "message": f"High pronoun density ({ratio:.1%}). Overusing pronouns (he, she, they) dilutes character focus. Replace some with the character's proper name.",
                "context": p_text[:80] + "..." if len(p_text) > 80 else p_text
            })

def main():
    parser = argparse.ArgumentParser(description="Brand Voice Linter for AI Publishing House.")
    parser.add_argument("file", help="Path to the draft manuscript markdown file.")
    parser.add_argument("--output", help="Optional output path to write a JSON report.")
    parser.add_argument("--json", action="store_true", help="Print the report to stdout in raw JSON format.")
    
    args = parser.parse_args()

    issues = analyze_file(args.file)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(issues, f, indent=2)
            print(f"Success: Report written to '{args.output}'")
        except Exception as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.json:
        print(json.dumps(issues, indent=2))
        return

    # Print a beautiful CLI report
    if not issues:
        print("Compliant! No Brand Voice violations found. Excellent work!")
        return

    print("=" * 60)
    print("      BRAND VOICE LINT REPORT - AI PUBLISHING HOUSE")
    print("=" * 60)
    
    warnings = [i for i in issues if i["severity"] == "WARNING"]
    infos = [i for i in issues if i["severity"] == "INFO"]
    
    print(f"Found {len(issues)} stylistic issues ({len(warnings)} Warnings, {len(infos)} Suggestions):\n")

    for issue in issues:
        color_tag = "[WARNING]" if issue["severity"] == "WARNING" else "[INFO]   "
        line_info = f"Line {issue['line']}: " if "line" in issue and issue["line"] else ""
        print(f"{color_tag} {line_info}{issue['message']}")
        print(f"  Context: \"{issue['context']}\"")
        print("-" * 60)

if __name__ == "__main__":
    main()
