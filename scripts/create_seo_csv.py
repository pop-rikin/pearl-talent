#!/usr/bin/env python3
"""
Script to create a CSV file with scraped SEO data from Pearl Talent resource pages.
"""

import csv
from datetime import datetime

# Scraped data from Firecrawl MCP
scraped_data = [
    {
        "url": "https://www.pearltalent.com/resources/executive-assistant-to-ceo-job-description",
        "title": "Comprehensive 2024 CEO Executive Assistant Job Description Template",
        "metadescription": "Providing a clear CEO executive assistant job description is essential to hiring a candidate who can give the CEO the most effective support. A well-crafted job description helps organizations attract qualified candidates who can contribute to the CEO's strategic goals and overall efficiency.",
        "h1": "Comprehensive 2024 CEO Executive Assistant Job Description Template"
    },
    {
        "url": "https://www.pearltalent.com/resources/executive-assistant-job-description",
        "title": "Executive Assistant Responsibilities: Skills, Duties, and a Free Template",
        "metadescription": "In today's fast-paced business world, organizations rely on skilled professionals to ensure smooth operations and effective management. Executive assistants support high-level executives and manage their busy schedules, making executive assistant responsibilities essential to overall efficiency.",
        "h1": "Executive Assistant Responsibilities: Skills, Duties, and a Free Template"
    },
    {
        "url": "https://www.pearltalent.com/resources/honest-review-of-taskus-a-2024-ultimate-guide",
        "title": "Honest Review of TaskUs: A 2024 Ultimate Guide",
        "metadescription": "Discover an in-depth review of TaskUs, a leading outsourcing company, and learn about its services, strengths, and areas for improvement. Get insights into customer experiences and recommendations for businesses considering outsourcing.",
        "h1": "Honest Review of TaskUs: A 2024 Ultimate Guide"
    },
    {
        "url": "https://www.pearltalent.com/resources/healthcare-virtual-assistant-hiring-platforms-7-sites",
        "title": "Healthcare Virtual Assistant Hiring Platforms: 7+ Sites",
        "metadescription": "The healthcare industry witnesses an escalating demand for efficient solutions, fostering a growing need for virtual healthcare assistants. These digital aides are pivotal in streamlining medical records, patient data, and administrative tasks, constituting a significant pillar within the healthcare sector.",
        "h1": "Healthcare Virtual Assistant Hiring Platforms: 7+ Sites"
    },
    {
        "url": "https://www.pearltalent.com/resources/administrative-assistant-skills",
        "title": "7+ Administrative Assistant Skills to Know Before Hiring",
        "metadescription": "Explore the essential administrative assistant skills needed for hiring top-tier candidates. Learn about organizational skills, communication, and more to streamline your hiring process.",
        "h1": "7+ Administrative Assistant Skills to Know Before Hiring"
    },
    {
        "url": "https://www.pearltalent.com/resources/hire-executive-assistant",
        "title": "16+ Best Sites to Hire Executive Assistants for Startups",
        "metadescription": "Discover the best platforms to hire executive assistants for startups. Explore top sites that connect you with skilled professionals to support your business needs.",
        "h1": "16+ Best Sites to Hire Executive Assistants for Startups"
    },
    {
        "url": "https://www.pearltalent.com/resources/types-of-outsourcing",
        "title": "9 Types Of Outsourcing: Pros & Cons | Identify The Best Fit",
        "metadescription": "Outsourcing is catching on like wildfire in today's business world. But you know what the real kicker is in all of this? Knowing the different types of outsourcing to see which will work best for you.",
        "h1": "9 Types Of Outsourcing: Pros & Cons | Identify The Best Fit"
    },
    {
        "url": "https://www.pearltalent.com/resources/virtual-assistant-cost",
        "title": "Virtual Assistant Cost: Calculating Ideal Hourly Costs 2024",
        "metadescription": "Discover the ideal hourly costs for hiring a virtual assistant in 2024. Learn about the factors affecting costs and how to calculate your total expenses effectively.",
        "h1": "Virtual Assistant Cost: Calculating Ideal Hourly Costs 2024"
    },
    {
        "url": "https://www.pearltalent.com/resources/best-calendar-management-tools",
        "title": "7+ Best Calendar Management Tools For Busy Executives",
        "metadescription": "Effective calendar management is crucial for maximizing productivity and staying organized in today's fast-paced world. Choosing the best calendar management tools can be overwhelming with the many options available. Here's a step-by-step guide to help you make the right choice:",
        "h1": "7+ Best Calendar Management Tools For Busy Executives"
    },
    {
        "url": "https://www.pearltalent.com/resources/personal-assistant-job-description",
        "title": "Personal Assistant Job Description: Role and Responsibilities",
        "metadescription": "Creating a personal assistant job description involves highlighting the role of supporting executives and managers in prioritizing task efficiency and managing daily operations. Personal assistants handle a variety of business tasks, allowing executives or top managers to concentrate on strategic decision-making.",
        "h1": "Personal Assistant Job Description: Role and Responsibilities"
    },
    {
        "url": "https://www.pearltalent.com/resources/remote-sales-representative",
        "title": "What Are the Advantages of Having a Remote Sales Representative?",
        "metadescription": "The rise of remote work has transformed how businesses operate. This shift has brought new opportunities for efficiency and flexibility. In the sales industry, remote sales representatives lead this change, offering a fresh approach to reaching customers.",
        "h1": "What Are the Advantages of Having a Remote Sales Representative?"
    }
]

def create_seo_csv():
    """Create CSV file with scraped SEO data."""
    
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"pearl_talent_seo_analysis_{timestamp}.csv"
    
    # CSV headers
    headers = ['URL', 'Title', 'Meta Description', 'H1', 'Title Length', 'Meta Description Length', 'H1 Length', 'Title = H1?']
    
    # Create CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for item in scraped_data:
            # Calculate additional metrics
            title_length = len(item['title'])
            meta_length = len(item['metadescription'])
            h1_length = len(item['h1'])
            title_equals_h1 = "Yes" if item['title'] == item['h1'] else "No"
            
            writer.writerow([
                item['url'],
                item['title'],
                item['metadescription'], 
                item['h1'],
                title_length,
                meta_length,
                h1_length,
                title_equals_h1
            ])
    
    print(f"✅ Created CSV file: {filename}")
    print(f"📊 Processed {len(scraped_data)} URLs")
    
    # Print summary statistics
    print("\n📈 SEO Analysis Summary:")
    print("=" * 50)
    
    avg_title_length = sum(len(item['title']) for item in scraped_data) / len(scraped_data)
    avg_meta_length = sum(len(item['metadescription']) for item in scraped_data) / len(scraped_data)
    avg_h1_length = sum(len(item['h1']) for item in scraped_data) / len(scraped_data)
    
    title_h1_matches = sum(1 for item in scraped_data if item['title'] == item['h1'])
    
    print(f"Average Title Length: {avg_title_length:.1f} characters")
    print(f"Average Meta Description Length: {avg_meta_length:.1f} characters")
    print(f"Average H1 Length: {avg_h1_length:.1f} characters")
    print(f"Title = H1 matches: {title_h1_matches}/{len(scraped_data)} ({title_h1_matches/len(scraped_data)*100:.1f}%)")
    
    print("\n📋 SEO Recommendations:")
    print("=" * 50)
    
    # Check for SEO issues
    long_titles = [item for item in scraped_data if len(item['title']) > 60]
    short_metas = [item for item in scraped_data if len(item['metadescription']) < 120]
    long_metas = [item for item in scraped_data if len(item['metadescription']) > 160]
    
    if long_titles:
        print(f"⚠️  {len(long_titles)} titles are longer than 60 characters")
    if short_metas:
        print(f"⚠️  {len(short_metas)} meta descriptions are shorter than 120 characters")
    if long_metas:
        print(f"⚠️  {len(long_metas)} meta descriptions are longer than 160 characters")
    
    if not (long_titles or short_metas or long_metas):
        print("✅ All pages follow basic SEO guidelines!")
    
    return filename

if __name__ == "__main__":
    print("Pearl Talent SEO Analysis Generator")
    print("=" * 50)
    create_seo_csv() 