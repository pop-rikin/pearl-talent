#!/usr/bin/env python3
"""
Generate Talent CSV for Airtable
Extracts structured data from talent profiles and creates a CSV file
"""

import os
import re
import csv
from pathlib import Path

def extract_talent_data(file_path):
    """Extract structured data from a talent profile"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Initialize data dictionary
    data = {
        'Name': '',
        'Location': '',
        'Country': '',
        'Region': '',
        'Role': '',
        'Experience_Years': '',
        'Previous_Company': '',
        'Specialization': '',
        'Status': '',
        'Skills': '',
        'Special_Expertise': '',
        'Testimonial': '',
        'File_Name': file_path.name
    }
    
    # Extract name
    name_match = re.search(r'# (.+)', content)
    if name_match:
        data['Name'] = name_match.group(1).strip()
    
    # Extract location and parse country/region
    location_match = re.search(r'\*\*Location:\*\* (.+)', content)
    if location_match:
        location = location_match.group(1).strip()
        data['Location'] = location
        
        # Parse country and region from location
        if '(' in location and ')' in location:
            # Format: "Argentina (Latin America)"
            country = location.split('(')[0].strip()
            region = location.split('(')[1].replace(')', '').strip()
            data['Country'] = country
            data['Region'] = region
        else:
            data['Country'] = location
    
    # Extract role
    role_match = re.search(r'\*\*Role:\*\* (.+)', content)
    if role_match:
        data['Role'] = role_match.group(1).strip()
    
    # Extract experience
    exp_match = re.search(r'\*\*Experience:\*\* (\d+)', content)
    if exp_match:
        data['Experience_Years'] = exp_match.group(1)
    
    # Extract previous company
    company_match = re.search(r'\*\*Previous Company:\*\* (.+)', content)
    if company_match:
        data['Previous_Company'] = company_match.group(1).strip()
    
    # Extract specialization
    spec_match = re.search(r'\*\*Specialization:\*\* (.+)', content)
    if spec_match:
        data['Specialization'] = spec_match.group(1).strip()
    
    # Extract status
    status_match = re.search(r'\*\*Status:\*\* (.+)', content)
    if status_match:
        data['Status'] = status_match.group(1).strip()
    
    # Extract skills (from Core Skills section)
    skills_match = re.search(r'## Core Skills\n(.*?)(?=##|$)', content, re.DOTALL)
    if skills_match:
        skills_text = skills_match.group(1).strip()
        # Convert bullet points to comma-separated list
        skills_list = []
        for line in skills_text.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                skills_list.append(line[2:].strip())
        data['Skills'] = ', '.join(skills_list)
    
    # Extract special expertise sections
    special_sections = []
    special_patterns = [
        r'## Healthcare Systems\n(.*?)(?=##|$)',
        r'## Technical Expertise\n(.*?)(?=##|$)',
        r'## Platform Experience\n(.*?)(?=##|$)',
        r'## Industry Experience\n(.*?)(?=##|$)',
        r'## Tools & Technologies\n(.*?)(?=##|$)'
    ]
    
    for pattern in special_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            section_content = match.group(0).replace('##', '').strip()
            special_sections.append(section_content)
    
    if special_sections:
        data['Special_Expertise'] = ' | '.join(special_sections)
    
    # Extract testimonial
    testimonial_match = re.search(r'\*"([^"]+)"\*', content)
    if testimonial_match:
        data['Testimonial'] = testimonial_match.group(1).strip()
    
    return data

def generate_talent_csv():
    """Generate CSV file from all talent profiles"""
    
    talent_dir = Path("Knowledge Base/07-talent")
    
    if not talent_dir.exists():
        print("❌ Talent directory not found")
        return
    
    print("📊 Generating talent CSV for Airtable...")
    
    # Collect all talent data
    talent_data = []
    
    for file_path in talent_dir.glob("*.md"):
        if file_path.name == "README.md":
            continue
            
        print(f"   📝 Processing {file_path.name}...")
        
        try:
            data = extract_talent_data(file_path)
            talent_data.append(data)
        except Exception as e:
            print(f"   ❌ Error processing {file_path.name}: {e}")
    
    # Sort by name
    talent_data.sort(key=lambda x: x['Name'])
    
    # Generate CSV
    csv_path = Path("templates/talent-profiles-airtable.csv")
    
    # Define field order for CSV
    fieldnames = [
        'Name',
        'Location',
        'Country', 
        'Region',
        'Role',
        'Experience_Years',
        'Previous_Company',
        'Specialization',
        'Status',
        'Skills',
        'Special_Expertise',
        'Testimonial',
        'File_Name'
    ]
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(talent_data)
    
    print(f"\n✅ Generated CSV with {len(talent_data)} talent profiles")
    print(f"📁 Saved to: {csv_path}")
    print("\n🎯 CSV Fields:")
    print("   - Name: Full name of talent")
    print("   - Location: Full location string")
    print("   - Country: Parsed country")
    print("   - Region: Parsed region (Latin America, Philippines, etc.)")
    print("   - Role: Current role seeking")
    print("   - Experience_Years: Years of experience (numeric)")
    print("   - Previous_Company: Last company worked at")
    print("   - Specialization: Area of expertise")
    print("   - Status: Availability status")
    print("   - Skills: Comma-separated list of core skills")
    print("   - Special_Expertise: Special sections (Healthcare Systems, etc.)")
    print("   - Testimonial: Client testimonial if available")
    print("   - File_Name: Source markdown file name")
    
    # Generate summary statistics
    print(f"\n📈 Summary Statistics:")
    
    # Count by region
    regions = {}
    roles = {}
    experience_ranges = {'0-2': 0, '3-5': 0, '6-10': 0, '10+': 0}
    
    for person in talent_data:
        # Count regions
        region = person['Region'] or 'Unknown'
        regions[region] = regions.get(region, 0) + 1
        
        # Count roles
        role = person['Role'] or 'Unknown'
        roles[role] = roles.get(role, 0) + 1
        
        # Count experience ranges
        try:
            exp = int(person['Experience_Years']) if person['Experience_Years'] else 0
            if exp <= 2:
                experience_ranges['0-2'] += 1
            elif exp <= 5:
                experience_ranges['3-5'] += 1
            elif exp <= 10:
                experience_ranges['6-10'] += 1
            else:
                experience_ranges['10+'] += 1
        except:
            pass
    
    print(f"   By Region: {dict(sorted(regions.items()))}")
    print(f"   By Experience: {experience_ranges}")
    print(f"   Top Roles: {dict(sorted(roles.items(), key=lambda x: x[1], reverse=True)[:5])}")

if __name__ == "__main__":
    generate_talent_csv() 