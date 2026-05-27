#!/usr/bin/env python3
"""
Manuscript Compiler for AI Publishing House.
Merges individual chapter files into a single, beautifully compiled master manuscript (Markdown or styled HTML),
complete with a dynamically generated Table of Contents.
"""

import argparse
import sys
import os
import re
import json

def get_natural_sort_key(s):
    """Sort strings containing numbers naturally, e.g., chapter_2.md comes before chapter_10.md"""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]

def extract_title_and_clean_content(file_path):
    """Reads a chapter file, strips frontmatter, and extracts the main heading as the title."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return "Unknown Chapter", ""

    # Normalize line endings
    content = content.replace("\r\n", "\n")

    # Strip YAML frontmatter if present
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2]

    # Find the first H1 or H2 as the title
    title = os.path.basename(file_path).replace(".md", "").replace("_", " ").title()
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if not title_match:
        title_match = re.search(r'^##\s+(.+)$', content, re.MULTILINE)
    
    if title_match:
        title = title_match.group(1).strip()
        # Remove the title heading from the content to avoid double headers when compiling
        content = content.replace(title_match.group(0), "", 1).strip()

    return title, content.strip()

def compile_manuscript(source_dir, output_file, format_type, index_file=None):
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # 1. Determine Chapter File List
    chapter_files = []
    if index_file and os.path.exists(index_file):
        try:
            with open(index_file, "r", encoding="utf-8") as f:
                index_data = json.load(f)
            chapter_files = [os.path.join(source_dir, f) for f in index_data.get("chapters", [])]
        except Exception as e:
            print(f"Error reading index file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Auto-discover chapter markdown files
        all_files = os.listdir(source_dir)
        chapter_candidates = [f for f in all_files if f.endswith(".md") and ("chapter" in f.lower() or f.split(".")[0].isdigit())]
        chapter_candidates.sort(key=get_natural_sort_key)
        chapter_files = [os.path.join(source_dir, f) for f in chapter_candidates]

    if not chapter_files:
        print(f"Warning: No chapter markdown files found in '{source_dir}'. Scanning all markdown files instead.")
        all_files = os.listdir(source_dir)
        markdown_files = [f for f in all_files if f.endswith(".md") and f not in ["manuscript_final.md", "README.md", "outline.md", "story_seed.md", "character_list.md", "world_map.md"]]
        markdown_files.sort(key=get_natural_sort_key)
        chapter_files = [os.path.join(source_dir, f) for f in markdown_files]

    if not chapter_files:
        print("Error: No markdown files found to compile.", file=sys.stderr)
        sys.exit(1)

    print(f"Compiling {len(chapter_files)} chapter files in order...")

    # 2. Extract Titles and Contents
    chapters_data = []
    for idx, filepath in enumerate(chapter_files):
        title, clean_content = extract_title_and_clean_content(filepath)
        chapters_data.append({
            "number": idx + 1,
            "title": title,
            "content": clean_content,
            "filename": os.path.basename(filepath)
        })
        print(f"  [{idx + 1}] {title} (from {os.path.basename(filepath)})")

    # 3. Build Table of Contents & Content String
    if format_type == "markdown":
        # Generate Markdown Manuscript
        compiled_str = "# Master Manuscript\n\n"
        compiled_str += "## Table of Contents\n\n"
        for ch in chapters_data:
            anchor = ch["title"].lower().replace(" ", "-").replace(":", "").replace("?", "").replace(",", "")
            compiled_str += f"- [{ch['title']}](#{anchor})\n"
        
        compiled_str += "\n---\n\n"

        for ch in chapters_data:
            compiled_str += f"# {ch['title']}\n\n"
            compiled_str += f"{ch['content']}\n\n"
            compiled_str += "---\n\n" # Page divider
        
        # Remove trailing divider
        compiled_str = compiled_str.rstrip("\n- ") + "\n"

    else:
        # Generate Styled HTML Manuscript
        css_style = """
        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #fbfbfb;
        }
        h1, h2, h3 {
            color: #0f172a;
            font-weight: 700;
        }
        h1 {
            font-size: 2.5em;
            margin-top: 1.5em;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.3em;
        }
        .toc {
            background-color: #f1f5f9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 40px;
            border: 1px solid #cbd5e1;
        }
        .toc ul {
            list-style-type: none;
            padding-left: 0;
        }
        .toc li {
            margin-bottom: 10px;
        }
        .toc a {
            color: #2563eb;
            text-decoration: none;
            font-weight: 500;
        }
        .toc a:hover {
            text-decoration: underline;
        }
        .chapter-divider {
            margin: 60px 0;
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0));
        }
        p {
            margin-bottom: 1.2em;
            text-indent: 1.5em;
        }
        p:first-of-type {
            text-indent: 0;
        }
        """
        
        compiled_str = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<title>Master Manuscript</title>\n<style>{css_style}</style>\n</head>\n<body>\n"
        compiled_str += "<h1>Master Manuscript</h1>\n"
        compiled_str += "<div class='toc'>\n<h2>Table of Contents</h2>\n<ul>\n"
        for ch in chapters_data:
            compiled_str += f"  <li><a href='#ch-{ch['number']}'>{ch['title']}</a></li>\n"
        compiled_str += "</ul>\n</div>\n\n"

        for idx, ch in enumerate(chapters_data):
            compiled_str += f"<section id='ch-{ch['number']}'>\n"
            compiled_str += f"  <h1>{ch['title']}</h1>\n"
            # Basic markdown to HTML converter for paragraphs and simple elements
            body_html = ch["content"]
            body_html = html_escape(body_html)
            # Separate by double newline into paragraphs
            paragraphs = body_html.split("\n\n")
            p_html_list = []
            for p in paragraphs:
                if p.strip():
                    # Handle minor bolding/italics markdown conversions
                    p_formatted = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p.strip())
                    p_formatted = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_formatted)
                    p_html_list.append(f"  <p>{p_formatted}</p>")
            compiled_str += "\n".join(p_html_list) + "\n"
            compiled_str += "</section>\n"
            if idx < len(chapters_data) - 1:
                compiled_str += "<hr class='chapter-divider'>\n\n"
        
        compiled_str += "</body>\n</html>\n"

    # 4. Write Output
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(compiled_str)
        print(f"Success! Compiled manuscript written to '{output_file}' (Format: {format_type})")
    except Exception as e:
        print(f"Error writing compiled manuscript: {e}", file=sys.stderr)
        sys.exit(1)

def html_escape(text):
    """A simple HTML escape that leaves basic layout characters, but escapes html-breaking entities."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def main():
    parser = argparse.ArgumentParser(description="Manuscript Compiler for AI Publishing House.")
    parser.add_argument("--source", default=".", help="Path to the directory containing chapter markdown files. Defaults to current directory.")
    parser.add_argument("--output", required=True, help="Path where the compiled manuscript should be saved.")
    parser.add_argument("--format", choices=["markdown", "html"], default="markdown", help="Output format: 'markdown' or 'html'. Defaults to 'markdown'.")
    parser.add_argument("--index", help="Optional path to a JSON index file defining chapter order explicitly (e.g. {'chapters': ['ch1.md', 'ch2.md']}).")

    args = parser.parse_args()

    compile_manuscript(args.source, args.output, args.format, args.index)

if __name__ == "__main__":
    main()
