import markdown
import argparse
import os
import sys
import html  # Add import for HTML escaping
import re  # Add import for regex support

def read_file(filepath):
    """Safely reads content from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {filepath}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate STDM Specification HTML from Markdown and Template.")
    parser.add_argument("markdown_file", help="Path to the input Markdown specification file (e.g., specification.md)")
    parser.add_argument("instructions_file", help="Path to the input STDM instructions file (e.g., stdm_instructions.txt)")
    parser.add_argument("template_file", help="Path to the HTML template file (e.g., template.html)")
    parser.add_argument("output_file", help="Path for the output HTML file (e.g., stdm_spec_v1.6.html)")

    args = parser.parse_args()

    # --- Read Input Files ---
    print(f"Reading Markdown spec from: {args.markdown_file}")
    markdown_text = read_file(args.markdown_file)

    print(f"Reading STDM instructions from: {args.instructions_file}")
    stdm_instructions_text = read_file(args.instructions_file)

    print(f"Reading HTML template from: {args.template_file}")
    template_html = read_file(args.template_file)

    # --- Convert Markdown to HTML ---
    print("Converting Markdown to HTML...")
    try:
        # Use extensions:
        # - fenced_code: For ``` blocks
        # - codehilite: For syntax highlighting (requires pygments)
        # - tables: For Markdown tables
        # - markdown.extensions.superscript: For handling ^superscript^ notation
        # - extra: Includes many useful features like footnotes, abbreviations, def lists, etc.
        #          Often includes fenced_code and tables implicitly.
        md_extensions = ['fenced_code', 'codehilite', 'tables', 'pymdownx.caret', 'extra']
        md = markdown.Markdown(extensions=md_extensions, output_format='html5')
        rendered_spec_html = md.convert(markdown_text)
        print("Markdown conversion successful.")
    except Exception as e:
        print(f"Error during Markdown conversion: {e}", file=sys.stderr)
        print("Ensure the 'markdown' and 'pygments' libraries are installed (`pip install markdown pygments`)", file=sys.stderr)
        sys.exit(1)


    # --- Interpolate Content into Template ---
    print("Interpolating content into template...")
    final_html = template_html

    # Replace comment block placeholders with escaped content to prevent HTML interpretation
    final_html = final_html.replace('{{stdm_instructions_block_content}}', html.escape(stdm_instructions_text))
    final_html = final_html.replace('{{specification_data_block_content}}', html.escape(markdown_text))

    # Replace the main content area with the Markdown-generated HTML
    # The markdown library should have already handled necessary internal escaping (e.g., for code blocks)
    final_html = final_html.replace('{{rendered_specification_html_content}}', rendered_spec_html)
    print("Interpolation complete.")

    # --- Write Output File ---
    print(f"Writing final HTML to: {args.output_file}")
    try:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Output file written successfully.")
    except Exception as e:
        print(f"Error writing output file {args.output_file}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
