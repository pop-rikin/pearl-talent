#!/usr/bin/env python3
"""
Script to update the CSV file with additional scraped SEO data from Pearl Talent resource pages.
"""

import csv
from datetime import datetime

# Updated scraped data from Firecrawl MCP (22 URLs total)
scraped_data = [
    # Original 11 URLs
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
    },
    # New 11 URLs added
    {
        "url": "https://www.pearltalent.com/resources/7-sites-to-search-for-medical-virtual-assistant-jobs-in-2023",
        "title": "9 Sites to Search for Virtual Medical Assistant Jobs in 2025",
        "metadescription": "In 2025, finding the right medical virtual assistant job can be incredibly challenging and time-consuming. Many qualified candidates waste weeks scrolling through generic job boards, only to find postings that don't match their healthcare experience or end up being scams.",
        "h1": "9 Sites to Search for Virtual Medical Assistant Jobs in 2025"
    },
    {
        "url": "https://www.pearltalent.com/resources/client-success-manager-role",
        "title": "What is a Client Success Manager? Role + Essential Skills",
        "metadescription": "A client success manager is crucial for customer-centric businesses, ensuring customers receive the support and guidance they need to fully utilize and benefit from a company's products or services.",
        "h1": "What is a Client Success Manager? Role + Essential Skills"
    },
    {
        "url": "https://www.pearltalent.com/resources/executive-assistant-job-description-examples-tips",
        "title": "Executive Assistant Job Description: Examples & Tips",
        "metadescription": "A practical executive assistant job description is crucial for any organization seeking to secure top talent and ensure smooth operations. Businesses can attract candidates who align with their needs and goals by clearly outlining the roles, responsibilities, required skills, and qualifications.",
        "h1": "Executive Assistant Job Description: Examples & Tips"
    },
    {
        "url": "https://www.pearltalent.com/resources/top-virtual-assistant-websites",
        "title": "11+ Top Virtual Assistant Websites in 2024",
        "metadescription": "Virtual assistants play a pivotal role across various industries today. They efficiently handle tasks like data entry, project management, social media management, email marketing, and much more, freeing up valuable time for businesses and entrepreneurs.",
        "h1": "11+ Top Virtual Assistant Websites in 2024"
    },
    {
        "url": "https://www.pearltalent.com/resources/amazon-virtual-assistant-jobs",
        "title": "Guide to Amazon Virtual Assistant Jobs: How to Get Started",
        "metadescription": "Explore the intricacies of Amazon virtual assistant jobs, including responsibilities, necessary skills, and how to excel in this dynamic role.",
        "h1": "Guide to Amazon Virtual Assistant Jobs: How to Get Started"
    },
    {
        "url": "https://www.pearltalent.com/resources/how-much-for-a-virtual-assistant-global-statistics-for-2023",
        "title": "How Much for a Virtual Assistant? Global Statistics for 2024",
        "metadescription": "Understanding how much for a virtual assistant is crucial for informed decision-making on a global scale. Paying virtual assistants varies across regions, skills, and payment structures.",
        "h1": "How Much for a Virtual Assistant? Global Statistics for 2024"
    },
    {
        "url": "https://www.pearltalent.com/resources/medical-billing-outsourcing-companies",
        "title": "Best 9+ Medical Billing Outsourcing Companies for 2024",
        "metadescription": "Selecting the right medical billing outsourcing company is crucial for the success of your healthcare practice. These top medical billing companies can significantly reduce administrative burdens and improve cash flow.",
        "h1": "Best 9+ Medical Billing Outsourcing Companies for 2024"
    },
    {
        "url": "https://www.pearltalent.com/resources/bookkeeping-services-for-small-businesses",
        "title": "7+ Sites to Hire Bookkeeping Services for Small Businesses",
        "metadescription": "Finding reliable bookkeeping services for small businesses remains a challenge, necessitating a guide to navigate the many options available.",
        "h1": "7+ Sites to Hire Bookkeeping Services for Small Businesses"
    },
    {
        "url": "https://www.pearltalent.com/resources/admin-assistant-job",
        "title": "What is an Admin Assistant: Job Description + 5 Benefits",
        "metadescription": "Explore the essential role of an admin assistant in modern workplaces, their responsibilities, and the benefits they bring to organizational efficiency.",
        "h1": "What is an Admin Assistant: Job Description + 5 Benefits"
    },
    {
        "url": "https://www.pearltalent.com/resources/outsourcing-strategy",
        "title": "Build Your Outsourcing Strategy in 5 Simple Steps + Examples",
        "metadescription": "A great outsourcing strategy gives you a way out of ineffective sticky situations by cutting costs, increasing efficiency, and accomplishing specialized tasks. But there are certain preliminaries you should follow – internal readiness assessments to ensure that it will benefit your organization in many ways.",
        "h1": "How To Build An Outsourcing Strategy In 5 Steps + Examples"
    },
    {
        "url": "https://www.pearltalent.com/resources/how-do-staffing-agencies-make-money",
        "title": "The Business Behind It: How Do Staffing Agencies Make Money",
        "metadescription": "Several businesses increasingly rely on staffing agencies to efficiently connect them with qualified candidates in a competitive job market. These agencies have become essential partners by managing the complexities of recruitment and placement, ensuring a good fit for both companies and job seekers.",
        "h1": "The Business Behind It: How Do Staffing Agencies Make Money"
    }
]

def create_updated_seo_csv():
    """Create updated CSV file with all scraped SEO data."""
    
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"pearl_talent_seo_analysis_updated_{timestamp}.csv"
    
    # CSV headers
    headers = ['URL', 'Title', 'Meta Description', 'H1', 'Title Length', 'Meta Description Length', 'H1 Length', 'Title = H1?', 'SEO Issues']
    
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
            
            # Identify SEO issues
            issues = []
            if title_length > 60:
                issues.append("Title too long")
            if meta_length > 160:
                issues.append("Meta desc too long")
            if meta_length < 120:
                issues.append("Meta desc too short")
            if item['title'] != item['h1']:
                issues.append("Title/H1 mismatch")
            
            seo_issues = "; ".join(issues) if issues else "None"
            
            writer.writerow([
                item['url'],
                item['title'],
                item['metadescription'], 
                item['h1'],
                title_length,
                meta_length,
                h1_length,
                title_equals_h1,
                seo_issues
            ])
    
    print(f"✅ Created updated CSV file: {filename}")
    print(f"📊 Processed {len(scraped_data)} URLs")
    
    # Print comprehensive summary statistics
    print("\n📈 Updated SEO Analysis Summary:")
    print("=" * 60)
    
    avg_title_length = sum(len(item['title']) for item in scraped_data) / len(scraped_data)
    avg_meta_length = sum(len(item['metadescription']) for item in scraped_data) / len(scraped_data)
    avg_h1_length = sum(len(item['h1']) for item in scraped_data) / len(scraped_data)
    
    title_h1_matches = sum(1 for item in scraped_data if item['title'] == item['h1'])
    title_h1_mismatches = len(scraped_data) - title_h1_matches
    
    print(f"📏 Average Title Length: {avg_title_length:.1f} characters")
    print(f"📏 Average Meta Description Length: {avg_meta_length:.1f} characters")
    print(f"📏 Average H1 Length: {avg_h1_length:.1f} characters")
    print(f"✅ Title = H1 matches: {title_h1_matches}/{len(scraped_data)} ({title_h1_matches/len(scraped_data)*100:.1f}%)")
    if title_h1_mismatches > 0:
        print(f"❌ Title ≠ H1 mismatches: {title_h1_mismatches}/{len(scraped_data)} ({title_h1_mismatches/len(scraped_data)*100:.1f}%)")
    
    # Detailed issue analysis
    print("\n🔍 Detailed SEO Issue Analysis:")
    print("=" * 60)
    
    long_titles = [item for item in scraped_data if len(item['title']) > 60]
    short_metas = [item for item in scraped_data if len(item['metadescription']) < 120]
    long_metas = [item for item in scraped_data if len(item['metadescription']) > 160]
    title_h1_diff = [item for item in scraped_data if item['title'] != item['h1']]
    
    print(f"⚠️  Long Titles (>60 chars): {len(long_titles)}/{len(scraped_data)} ({len(long_titles)/len(scraped_data)*100:.1f}%)")
    print(f"⚠️  Short Meta Descriptions (<120 chars): {len(short_metas)}/{len(scraped_data)} ({len(short_metas)/len(scraped_data)*100:.1f}%)")
    print(f"⚠️  Long Meta Descriptions (>160 chars): {len(long_metas)}/{len(scraped_data)} ({len(long_metas)/len(scraped_data)*100:.1f}%)")
    print(f"⚠️  Title/H1 Mismatches: {len(title_h1_diff)}/{len(scraped_data)} ({len(title_h1_diff)/len(scraped_data)*100:.1f}%)")
    
    # Progress tracking
    print(f"\n🚀 Progress Tracking:")
    print("=" * 60)
    print(f"📊 URLs Processed: {len(scraped_data)}/74 ({len(scraped_data)/74*100:.1f}%)")
    print(f"🔄 Remaining URLs: {74 - len(scraped_data)}")
    print(f"📈 Batch Progress: Added 11 new URLs in this session")
    
    if title_h1_diff:
        print(f"\n📋 Title/H1 Mismatches Found:")
        for item in title_h1_diff:
            print(f"   • {item['url'].split('/')[-1]}")
    
    return filename

if __name__ == "__main__":
    print("Pearl Talent SEO Analysis Updater")
    print("=" * 60)
    create_updated_seo_csv() 