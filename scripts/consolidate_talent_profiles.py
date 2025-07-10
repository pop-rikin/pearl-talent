#!/usr/bin/env python3
"""
Consolidate Talent Profiles
Removes repetitive information from individual talent files
"""

import os
import re
from pathlib import Path

def consolidate_talent_profile(file_path):
    """Consolidate a single talent profile to remove repetition"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract key information
    name_match = re.search(r'# (.+)', content)
    name = name_match.group(1) if name_match else "Unknown"
    
    # Extract location
    location_match = re.search(r'\*\*Current Location:\*\* (.+)', content)
    if not location_match:
        location_match = re.search(r'\*\*Location:\*\* (.+)', content)
    location = location_match.group(1) if location_match else "Unknown"
    
    # Extract region
    region_match = re.search(r'\*\*Region:\*\* (.+)', content)
    region = region_match.group(1) if region_match else ""
    
    # Combine location and region
    if region and region not in location:
        full_location = f"{location} ({region.replace('(', '').replace(')', '')})"
    else:
        full_location = location
    
    # Extract role
    role_matches = [
        re.search(r'\*\*Current Role Seeking:\*\* (.+)', content),
        re.search(r'\*\*Current Role:\*\* (.+)', content),
        re.search(r'\*\*Position:\*\* (.+)', content),
        re.search(r'\*\*Role:\*\* (.+)', content)
    ]
    role = None
    for match in role_matches:
        if match:
            role = match.group(1)
            break
    
    # Extract years of experience (find first occurrence)
    exp_matches = [
        re.search(r'\*\*Years of Experience:\*\* (\d+)', content),
        re.search(r'(\d+) years', content),
        re.search(r'\*\*Experience:\*\* (\d+)', content)
    ]
    experience = None
    for match in exp_matches:
        if match:
            experience = match.group(1)
            break
    
    # Extract previous company
    prev_company_match = re.search(r'\*\*Previous Company:\*\* (.+)', content)
    prev_company = prev_company_match.group(1) if prev_company_match else ""
    
    # Extract current company (for placed talent)
    current_company_match = re.search(r'\*\*Company:\*\* (.+)', content)
    current_company = current_company_match.group(1) if current_company_match else ""
    
    # Extract specialization
    spec_matches = [
        re.search(r'\*\*Specialization:\*\* (.+)', content),
        re.search(r'\*\*Technical Focus:\*\* (.+)', content)
    ]
    specialization = None
    for match in spec_matches:
        if match:
            specialization = match.group(1)
            break
    
    # Determine status
    if "Successfully placed" in content or current_company:
        status = "Placed (Pearl Talent Alumni)"
    elif "Available for hire" in content or "Available for placement" in content:
        status = "Available for placement"
    else:
        status = "Status unknown"
    
    # Extract skills (look for skills sections)
    skills_section = ""
    skills_patterns = [
        r'## Skills and Expertise\n(.*?)(?=##|$)',
        r'## Core Skills\n(.*?)(?=##|$)',
        r'## Technical Skills\n(.*?)(?=##|$)'
    ]
    
    for pattern in skills_patterns:
        skills_match = re.search(pattern, content, re.DOTALL)
        if skills_match:
            skills_section = skills_match.group(1).strip()
            break
    
    # Extract testimonial if exists
    testimonial_match = re.search(r'\*"([^"]+)"\*', content)
    testimonial = testimonial_match.group(1) if testimonial_match else ""
    
    # Build consolidated content
    consolidated = f"# {name}\n\n"
    consolidated += "## Basic Information\n"
    consolidated += f"- **Name:** {name}\n"
    consolidated += f"- **Location:** {full_location}\n"
    
    if role:
        consolidated += f"- **Role:** {role}\n"
    
    if experience:
        role_context = ""
        if "Executive Assistant" in (role or ""):
            role_context = " in executive assistance"
        elif "Developer" in (role or "") or "Engineer" in (role or ""):
            role_context = " in software development"
        elif "Designer" in (role or ""):
            role_context = " in design"
        elif "QA" in (role or ""):
            role_context = " in quality assurance"
        elif "Marketing" in (role or ""):
            role_context = " in marketing"
        elif "Healthcare" in content or "Patient" in (role or "") or "Telemedicine" in (role or ""):
            role_context = " in healthcare coordination"
        elif "Insurance" in (role or ""):
            role_context = " in insurance/healthcare"
        
        consolidated += f"- **Experience:** {experience} years{role_context}\n"
    
    if prev_company:
        consolidated += f"- **Previous Company:** {prev_company}\n"
    
    if current_company:
        consolidated += f"- **Current Company:** {current_company}\n"
    
    if specialization:
        consolidated += f"- **Specialization:** {specialization}\n"
    
    consolidated += f"- **Status:** {status}\n"
    
    # Add testimonial if exists
    if testimonial:
        consolidated += f"\n## Testimonial\n*\"{testimonial}\"*\n"
    
    # Add skills if found
    if skills_section:
        consolidated += f"\n## Core Skills\n{skills_section}\n"
    
    return consolidated

def main():
    """Consolidate all talent profiles"""
    
    talent_dir = Path("Knowledge Base/07-talent")
    
    if not talent_dir.exists():
        print("❌ Talent directory not found")
        return
    
    print("🔄 Consolidating talent profiles...")
    
    consolidated_count = 0
    
    for file_path in talent_dir.glob("*.md"):
        if file_path.name == "README.md":
            continue
            
        print(f"   📝 Processing {file_path.name}...")
        
        try:
            consolidated_content = consolidate_talent_profile(file_path)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(consolidated_content)
            
            consolidated_count += 1
            
        except Exception as e:
            print(f"   ❌ Error processing {file_path.name}: {e}")
    
    print(f"\n✅ Consolidated {consolidated_count} talent profiles")
    print("🎯 Removed repetitive information:")
    print("   - Multiple years of experience mentions")
    print("   - Duplicate status fields") 
    print("   - Redundant location information")
    print("   - Repetitive Pearl Talent references")

if __name__ == "__main__":
    main() 