import json
import os
from jinja2 import Template
import math

def load_roles():
    with open('content/hiring/roles.json', 'r') as f:
        return json.load(f)['roles']

def load_template():
    with open('content/hiring/template.md', 'r') as f:
        return Template(f.read())

def format_skills_list(skills):
    if len(skills) == 1:
        return skills[0]
    elif len(skills) == 2:
        return f"{skills[0]} and {skills[1]}"
    else:
        return ", ".join(skills[:-1]) + f", and {skills[-1]}"

def format_interview_questions(questions):
    formatted = []
    for category in questions:
        formatted.append(f"### {category['category']} Questions\n")
        for q in category['questions']:
            formatted.append(f"- {q}")
        formatted.append("\n")
    return "\n".join(formatted)

def format_job_description(template):
    formatted = []
    formatted.append("### Requirements")
    for req in template['requirements']:
        formatted.append(f"- {req}")
    formatted.append("\n### Responsibilities")
    for resp in template['responsibilities']:
        formatted.append(f"- {resp}")
    return "\n".join(formatted)

def calculate_savings(salary_range):
    yearly_savings = salary_range['us_yearly'] - salary_range['latam_yearly']
    savings_percentage = math.floor((yearly_savings / salary_range['us_yearly']) * 100)
    return yearly_savings, savings_percentage

def generate_article(role_data, template):
    # Add computed fields
    for exp in role_data['experience_levels']:
        exp['skills_list'] = format_skills_list(exp['skills'])
    
    yearly_savings, savings_percentage = calculate_savings(role_data['salary_range'])
    role_data['yearly_savings'] = yearly_savings
    role_data['savings_percentage'] = savings_percentage
    
    # Format interview questions and job description
    role_data['formatted_interview_questions'] = format_interview_questions(role_data['interview_questions'])
    role_data['formatted_job_description'] = format_job_description(role_data['job_description_template'])
    
    # Generate content
    content = template.render(**role_data, role=role_data['title'])
    
    # Create output directory if it doesn't exist
    os.makedirs('content/hiring/generated', exist_ok=True)
    
    # Write to file
    output_file = f"content/hiring/generated/{role_data['slug']}.md"
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Generated hiring article for {role_data['title']}")

def main():
    roles = load_roles()
    template = load_template()
    
    for role in roles:
        generate_article(role, template)

if __name__ == "__main__":
    main() 