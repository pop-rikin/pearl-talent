import csv
import os
import re

def parse_markdown_outline(file_path):
    role_from_h1 = ""
    sections = {}
    current_normalized_section_title = None
    content_buffer = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Extract Role from H1
            if line.startswith("# Hire the Top 2% of Remote"):
                match = re.search(r"# Hire the Top 2% of Remote (.*)", line)
                if match:
                    role_from_h1 = match.group(1).strip()
                continue

            # New section header
            if line.startswith("## "):
                # Store the content of the PREVIOUS section using its normalized title
                if current_normalized_section_title and content_buffer:
                    sections[current_normalized_section_title] = "\n".join(content_buffer)
                
                # Process the NEW section title
                raw_section_title = line[3:].strip()
                normalized_title = raw_section_title # Default if no role name is found in it

                if role_from_h1: # Ensure role_from_h1 is set
                    role_variations = [role_from_h1]
                    # Add singular form if role_from_h1 seems plural and ends with 's'
                    if role_from_h1.endswith('s') and len(role_from_h1) > 1:
                        singular_candidate = role_from_h1[:-1]
                        # Avoid adding if it's identical (e.g. role is "Data Ops")
                        if singular_candidate != role_from_h1:
                             role_variations.append(singular_candidate)
                    
                    # Sort by length, longest first, to prioritize more specific matches
                    # e.g., match "UI/UX Designer" before "Designer" if both were generated
                    role_variations.sort(key=len, reverse=True)

                    for var in role_variations:
                        if var in raw_section_title: # Case-sensitive check
                            # Replace the specific role name variant with "{{ Role }}"
                            normalized_title = raw_section_title.replace(var, "{{ Role }}")
                            break # Stop after the first (longest) match

                current_normalized_section_title = normalized_title
                content_buffer = []
            # Content under a section
            elif line.startswith("- ") and current_normalized_section_title:
                content_buffer.append(line[2:].strip())
            # Other lines within a section that are not list items (but still part of content)
            elif current_normalized_section_title and line and not line.startswith("## ") and not line.startswith("#"):
                 content_buffer.append(line.strip())

    # Add the last section's content
    if current_normalized_section_title and content_buffer:
        sections[current_normalized_section_title] = "\n".join(content_buffer)
    
    return role_from_h1, sections

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the outline_dir relative to the script_dir
    outline_dir = os.path.join(script_dir, "../content/hiring")
    all_data = []
    all_section_headers = set()
    
    # First pass: Collect all data and section headers
    for root, _, files in os.walk(outline_dir):
        for file_name in files:
            if file_name == "outline.md":
                file_path = os.path.join(root, file_name)
                role, sections = parse_markdown_outline(file_path)
                if role and sections:
                    all_data.append({"role": role, "sections": sections})
                    all_section_headers.update(sections.keys())

    if not all_data:
        print("No outline.md files found or parsed.")
        return

    # Prepare CSV
    # Sort headers for consistent column order, though set itself is unordered
    # It's good practice to have a defined order for CSV columns.
    sorted_section_headers = sorted(list(all_section_headers))
    # Construct the path to the csv_file_path relative to the script_dir, placing it in the workspace root
    csv_file_path = os.path.join(script_dir, "../outline_summary.csv")

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Role'] + sorted_section_headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in all_data:
            row = {'Role': item['role']}
            for header in sorted_section_headers:
                row[header] = item['sections'].get(header, "") # Get content or empty string if section not present for this role
            writer.writerow(row)
            
    print(f"CSV file created at {csv_file_path}")

if __name__ == "__main__":
    main() 