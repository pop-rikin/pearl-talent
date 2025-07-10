#!/usr/bin/env python3
"""
Clean Talent Profiles
Removes redundant information and consolidates talent profiles
"""

import os
import re
from pathlib import Path

def clean_talent_profile(file_path):
    """Clean a single talent profile to remove redundancy"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract key information
    name_match = re.search(r'# (.+)', content)
    name = name_match.group(1) if name_match else "Unknown"
    
    # Extract location (combine current location and region)
    location_match = re.search(r'\*\*Current Location:\*\* (.+)', content)
    region_match = re.search(r'\*\*Region:\*\* (.+)', content)
    
    if location_match and region_match:
        location = location_match.group(1)
        region = region_match.group(1).replace('(', '').replace(')', '')
        if region not in location:
            full_location = f"{location} ({region})"
        else:
            full_location = location
    elif location_match:
        full_location = location_match.group(1)
    else:
        full_location = "Unknown"
    
    # Extract role (use "Current Role Seeking" as primary)
    role_match = re.search(r'\*\*Current Role Seeking:\*\* (.+)', content)
    role = role_match.group(1) if role_match else "Unknown"
    
    # Extract years of experience (first occurrence)
    exp_match = re.search(r'\*\*Years of Experience:\*\* (\d+)', content)
    experience = exp_match.group(1) if exp_match else None
    
    # Extract previous company
    prev_company_match = re.search(r'\*\*Previous Company:\*\* (.+)', content)
    prev_company = prev_company_match.group(1) if prev_company_match else None
    
    # Extract specialization
    spec_match = re.search(r'\*\*Specialization:\*\* (.+)', content)
    specialization = spec_match.group(1) if spec_match else None
    
    # Extract skills section
    skills_patterns = [
        r'## Skills and Expertise\n(.*?)(?=##|$)',
        r'## Core Skills\n(.*?)(?=##|$)',
        r'## Technical Skills\n(.*?)(?=##|$)'
    ]
    
    skills_section = ""
    for pattern in skills_patterns:
        skills_match = re.search(pattern, content, re.DOTALL)
        if skills_match:
            skills_section = skills_match.group(1).strip()
            break
    
    # Extract any special sections (like Healthcare Systems, Technical Expertise, etc.)
    special_sections = []
    
    # Look for specific expertise sections
    special_patterns = [
        (r'## Healthcare Systems Experience\n(.*?)(?=##|$)', 'Healthcare Systems'),
        (r'## Technical Expertise\n(.*?)(?=##|$)', 'Technical Expertise'),
        (r'## Platform Experience\n(.*?)(?=##|$)', 'Platform Experience'),
        (r'## Industry Experience\n(.*?)(?=##|$)', 'Industry Experience'),
        (r'## Tools & Technologies\n(.*?)(?=##|$)', 'Tools & Technologies')
    ]
    
    for pattern, section_name in special_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            special_sections.append((section_name, match.group(1).strip()))
    
    # Extract testimonial if exists
    testimonial_match = re.search(r'\*"([^"]+)"\*', content)
    testimonial = testimonial_match.group(1) if testimonial_match else None
    
    # Build clean, consolidated content
    cleaned = f"# {name}\n\n"
    
    # Basic Information (consolidated)
    cleaned += "## Profile Overview\n"
    cleaned += f"- **Location:** {full_location}\n"
    cleaned += f"- **Role:** {role}\n"
    
    if experience:
        cleaned += f"- **Experience:** {experience} years\n"
    
    if prev_company:
        cleaned += f"- **Previous Company:** {prev_company}\n"
    
    if specialization:
        cleaned += f"- **Specialization:** {specialization}\n"
    
    cleaned += "- **Status:** Available for placement\n"
    
    # Add testimonial if exists
    if testimonial:
        cleaned += f"\n## Client Testimonial\n*\"{testimonial}\"*\n"
    
    # Add special sections if they exist
    for section_name, section_content in special_sections:
        cleaned += f"\n## {section_name}\n{section_content}\n"
    
    # Add skills if found
    if skills_section:
        cleaned += f"\n## Core Skills\n{skills_section}\n"
    
    return cleaned

def main():
    """Clean all talent profiles"""
    
    talent_dir = Path("Knowledge Base/07-talent")
    
    if not talent_dir.exists():
        print("❌ Talent directory not found")
        return
    
    print("🧹 Cleaning talent profiles...")
    
    cleaned_count = 0
    
    for file_path in talent_dir.glob("*.md"):
        if file_path.name == "README.md":
            continue
            
        print(f"   📝 Cleaning {file_path.name}...")
        
        try:
            cleaned_content = clean_talent_profile(file_path)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            cleaned_count += 1
            
        except Exception as e:
            print(f"   ❌ Error cleaning {file_path.name}: {e}")
    
    print(f"\n✅ Cleaned {cleaned_count} talent profiles")
    print("🎯 Removed redundant information:")
    print("   - Duplicate experience mentions")
    print("   - Repeated company information")
    print("   - Multiple status fields")
    print("   - Redundant location data")
    print("   - Duplicate role descriptions")

if __name__ == "__main__":
    main() 