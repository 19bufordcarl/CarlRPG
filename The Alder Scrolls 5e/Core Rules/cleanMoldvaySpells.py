#!/usr/bin/env python3
"""
clean_spells.py

Cleans up a Moldvay spells Markdown file:
- Converts metadata headings to bold lines.
- Fixes spell name headings to level 2.
- Converts bullet headings to Markdown lists.
- Bolds level/category lines after spell names.
- Merges broken lines inside spell descriptions into single paragraphs.
- Preserves lists, tables, and headings.
- Normalises blank lines.

Usage:
    python clean_spells.py input.md output.md
"""

import re
import sys

def clean_moldvay_spells(text: str) -> str:
    # ------------------------------------------------------------
    # First pass: structural cleanup (headings, metadata, lists)
    # ------------------------------------------------------------
    lines = text.split('\n')
    first_pass = []
    prev_non_empty = ''

    for line in lines:
        stripped = line.rstrip()

        # Metadata headings -> bold lines
        m = re.match(r'^###\s+(Casting Time|Range|Target|Targets|Duration):\s*(.*)$',
                     stripped, re.IGNORECASE)
        if m:
            key = m.group(1).strip()
            value = m.group(2).strip()
            out_line = f"**{key}:** {value}"
            first_pass.append(out_line)
            prev_non_empty = out_line
            continue

        # Bullet-like headings (### • …)
        if stripped.startswith('### •'):
            content = stripped[4:].strip().lstrip('• ').strip()
            for label in ['AC', 'Hit Points', 'Tests', 'Brachiation']:
                if content.lower().startswith(label.lower() + '.'):
                    rest = content[len(label)+1:].strip()
                    out_line = f"- **{label}.** {rest}"
                    break
            else:
                out_line = f"- {content}"
            first_pass.append(out_line)
            prev_non_empty = out_line
            continue

        # Level headers (### Level X. …)
        m = re.match(r'^###\s+(Level\s+\d+\.\s*.*)$', stripped, re.IGNORECASE)
        if m:
            out_line = f"**{m.group(1)}**"
            first_pass.append(out_line)
            prev_non_empty = out_line
            continue

        # Command options (### Approach. … etc.)
        m = re.match(r'^###\s+(Approach|Fight|Flee|Grovel|Halt)\.\s*(.*)$',
                     stripped, re.IGNORECASE)
        if m:
            cmd = m.group(1).capitalize()
            rest = m.group(2).strip()
            out_line = f"- **{cmd}.** {rest}"
            first_pass.append(out_line)
            prev_non_empty = out_line
            continue

        # Spell name headings (### Something) -> ## Something
        if stripped.startswith('### '):
            content = stripped[4:].strip()
            if re.match(r'^(Casting Time|Range|Target|Targets|Duration):', content, re.IGNORECASE):
                pass  # already handled
            else:
                out_line = f"## {content}"
                first_pass.append(out_line)
                prev_non_empty = out_line
            continue

        # Normal line
        if stripped:
            # Bold the level/category line if it directly follows a spell name
            if prev_non_empty.startswith('## ') and re.match(
                    r'^(Level\s+\d+|.*Cantrip|.*\(.*\))$', stripped):
                out_line = f"**{stripped}**"
            else:
                out_line = stripped
            first_pass.append(out_line)
            prev_non_empty = out_line
        else:
            # Preserve blank line (we will handle paragraph merging later)
            if first_pass and first_pass[-1] != '':
                first_pass.append('')

    # ------------------------------------------------------------
    # Second pass: merge broken lines into paragraphs
    # ------------------------------------------------------------
    blocks = []
    para_buffer = []

    def flush_para():
        if para_buffer:
            # Join with spaces, collapse multiple spaces
            para_text = ' '.join(para_buffer)
            para_text = re.sub(r'\s+', ' ', para_text).strip()
            if para_text:
                blocks.append(para_text)
            para_buffer.clear()

    # Patterns for lines that should NOT be merged into a paragraph
    special_patterns = [
        re.compile(r'^##\s'),           # spell heading
        re.compile(r'^\*\*'),           # bold metadata / level note
        re.compile(r'^-\s'),            # list item
        re.compile(r'^\|'),             # table row
        re.compile(r'^###\s'),          # any leftover heading
    ]

    for line in first_pass:
        stripped = line.strip()
        if not stripped:
            continue  # ignore blank lines – they are just artifacts

        is_special = any(p.match(stripped) for p in special_patterns)
        if is_special:
            flush_para()
            blocks.append(stripped)
        else:
            para_buffer.append(stripped)

    flush_para()  # flush any remaining paragraph

    # ------------------------------------------------------------
    # Rebuild output with proper spacing
    # ------------------------------------------------------------
    output = []
    for block in blocks:
        output.append(block)
        output.append('')  # blank line after each block

    result = '\n'.join(output)
    result = re.sub(r'\n{3,}', '\n\n', result)  # collapse multiple blanks
    return result.strip() + '\n'


def main():
    if len(sys.argv) != 3:
        print("Usage: python clean_spells.py input.md output.md")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    cleaned = clean_moldvay_spells(text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f"Cleaned Markdown written to {output_path}")


if __name__ == '__main__':
    main()