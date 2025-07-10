#!/usr/bin/env python3
"""
Comprehensive Pearl Talent SEO Analysis - 33 URLs Complete
"""

import csv
from datetime import datetime

# All 33 scraped URLs with complete data
scraped_data = [
    # Batch 1 (Original 11)
    {"url": "https://www.pearltalent.com/resources/executive-assistant-to-ceo-job-description", "title": "Comprehensive 2024 CEO Executive Assistant Job Description Template", "metadescription": "Providing a clear CEO executive assistant job description is essential to hiring a candidate who can give the CEO the most effective support. A well-crafted job description helps organizations attract qualified candidates who can contribute to the CEO's strategic goals and overall efficiency.", "h1": "Comprehensive 2024 CEO Executive Assistant Job Description Template"},
    {"url": "https://www.pearltalent.com/resources/executive-assistant-job-description", "title": "Executive Assistant Responsibilities: Skills, Duties, and a Free Template", "metadescription": "In today's fast-paced business world, organizations rely on skilled professionals to ensure smooth operations and effective management. Executive assistants support high-level executives and manage their busy schedules, making executive assistant responsibilities essential to overall efficiency.", "h1": "Executive Assistant Responsibilities: Skills, Duties, and a Free Template"},
    {"url": "https://www.pearltalent.com/resources/honest-review-of-taskus-a-2024-ultimate-guide", "title": "Honest Review of TaskUs: A 2024 Ultimate Guide", "metadescription": "Discover an in-depth review of TaskUs, a leading outsourcing company, and learn about its services, strengths, and areas for improvement. Get insights into customer experiences and recommendations for businesses considering outsourcing.", "h1": "Honest Review of TaskUs: A 2024 Ultimate Guide"},
    {"url": "https://www.pearltalent.com/resources/healthcare-virtual-assistant-hiring-platforms-7-sites", "title": "Healthcare Virtual Assistant Hiring Platforms: 7+ Sites", "metadescription": "The healthcare industry witnesses an escalating demand for efficient solutions, fostering a growing need for virtual healthcare assistants. These digital aides are pivotal in streamlining medical records, patient data, and administrative tasks, constituting a significant pillar within the healthcare sector.", "h1": "Healthcare Virtual Assistant Hiring Platforms: 7+ Sites"},
    {"url": "https://www.pearltalent.com/resources/administrative-assistant-skills", "title": "7+ Administrative Assistant Skills to Know Before Hiring", "metadescription": "Explore the essential administrative assistant skills needed for hiring top-tier candidates. Learn about organizational skills, communication, and more to streamline your hiring process.", "h1": "7+ Administrative Assistant Skills to Know Before Hiring"},
    {"url": "https://www.pearltalent.com/resources/hire-executive-assistant", "title": "16+ Best Sites to Hire Executive Assistants for Startups", "metadescription": "Discover the best platforms to hire executive assistants for startups. Explore top sites that connect you with skilled professionals to support your business needs.", "h1": "16+ Best Sites to Hire Executive Assistants for Startups"},
    {"url": "https://www.pearltalent.com/resources/types-of-outsourcing", "title": "9 Types Of Outsourcing: Pros & Cons | Identify The Best Fit", "metadescription": "Outsourcing is catching on like wildfire in today's business world. But you know what the real kicker is in all of this? Knowing the different types of outsourcing to see which will work best for you.", "h1": "9 Types Of Outsourcing: Pros & Cons | Identify The Best Fit"},
    {"url": "https://www.pearltalent.com/resources/virtual-assistant-cost", "title": "Virtual Assistant Cost: Calculating Ideal Hourly Costs 2024", "metadescription": "Discover the ideal hourly costs for hiring a virtual assistant in 2024. Learn about the factors affecting costs and how to calculate your total expenses effectively.", "h1": "Virtual Assistant Cost: Calculating Ideal Hourly Costs 2024"},
    {"url": "https://www.pearltalent.com/resources/best-calendar-management-tools", "title": "7+ Best Calendar Management Tools For Busy Executives", "metadescription": "Effective calendar management is crucial for maximizing productivity and staying organized in today's fast-paced world. Choosing the best calendar management tools can be overwhelming with the many options available. Here's a step-by-step guide to help you make the right choice:", "h1": "7+ Best Calendar Management Tools For Busy Executives"},
    {"url": "https://www.pearltalent.com/resources/personal-assistant-job-description", "title": "Personal Assistant Job Description: Role and Responsibilities", "metadescription": "Creating a personal assistant job description involves highlighting the role of supporting executives and managers in prioritizing task efficiency and managing daily operations. Personal assistants handle a variety of business tasks, allowing executives or top managers to concentrate on strategic decision-making.", "h1": "Personal Assistant Job Description: Role and Responsibilities"},
    {"url": "https://www.pearltalent.com/resources/remote-sales-representative", "title": "What Are the Advantages of Having a Remote Sales Representative?", "metadescription": "The rise of remote work has transformed how businesses operate. This shift has brought new opportunities for efficiency and flexibility. In the sales industry, remote sales representatives lead this change, offering a fresh approach to reaching customers.", "h1": "What Are the Advantages of Having a Remote Sales Representative?"},
    
    # Batch 2 (URLs 12-22)
    {"url": "https://www.pearltalent.com/resources/7-sites-to-search-for-medical-virtual-assistant-jobs-in-2023", "title": "9 Sites to Search for Virtual Medical Assistant Jobs in 2025", "metadescription": "In 2025, finding the right medical virtual assistant job can be incredibly challenging and time-consuming. Many qualified candidates waste weeks scrolling through generic job boards, only to find postings that don't match their healthcare experience or end up being scams.", "h1": "9 Sites to Search for Virtual Medical Assistant Jobs in 2025"},
    {"url": "https://www.pearltalent.com/resources/client-success-manager-role", "title": "What is a Client Success Manager? Role + Essential Skills", "metadescription": "A client success manager is crucial for customer-centric businesses, ensuring customers receive the support and guidance they need to fully utilize and benefit from a company's products or services.", "h1": "What is a Client Success Manager? Role + Essential Skills"},
    {"url": "https://www.pearltalent.com/resources/executive-assistant-job-description-examples-tips", "title": "Executive Assistant Job Description: Examples & Tips", "metadescription": "A practical executive assistant job description is crucial for any organization seeking to secure top talent and ensure smooth operations. Businesses can attract candidates who align with their needs and goals by clearly outlining the roles, responsibilities, required skills, and qualifications.", "h1": "Executive Assistant Job Description: Examples & Tips"},
    {"url": "https://www.pearltalent.com/resources/top-virtual-assistant-websites", "title": "11+ Top Virtual Assistant Websites in 2024", "metadescription": "Virtual assistants play a pivotal role across various industries today. They efficiently handle tasks like data entry, project management, social media management, email marketing, and much more, freeing up valuable time for businesses and entrepreneurs.", "h1": "11+ Top Virtual Assistant Websites in 2024"},
    {"url": "https://www.pearltalent.com/resources/amazon-virtual-assistant-jobs", "title": "Guide to Amazon Virtual Assistant Jobs: How to Get Started", "metadescription": "Explore the intricacies of Amazon virtual assistant jobs, including responsibilities, necessary skills, and how to excel in this dynamic role.", "h1": "Guide to Amazon Virtual Assistant Jobs: How to Get Started"},
    {"url": "https://www.pearltalent.com/resources/how-much-for-a-virtual-assistant-global-statistics-for-2023", "title": "How Much for a Virtual Assistant? Global Statistics for 2024", "metadescription": "Understanding how much for a virtual assistant is crucial for informed decision-making on a global scale. Paying virtual assistants varies across regions, skills, and payment structures.", "h1": "How Much for a Virtual Assistant? Global Statistics for 2024"},
    {"url": "https://www.pearltalent.com/resources/medical-billing-outsourcing-companies", "title": "Best 9+ Medical Billing Outsourcing Companies for 2024", "metadescription": "Selecting the right medical billing outsourcing company is crucial for the success of your healthcare practice. These top medical billing companies can significantly reduce administrative burdens and improve cash flow.", "h1": "Best 9+ Medical Billing Outsourcing Companies for 2024"},
    {"url": "https://www.pearltalent.com/resources/bookkeeping-services-for-small-businesses", "title": "7+ Sites to Hire Bookkeeping Services for Small Businesses", "metadescription": "Finding reliable bookkeeping services for small businesses remains a challenge, necessitating a guide to navigate the many options available.", "h1": "7+ Sites to Hire Bookkeeping Services for Small Businesses"},
    {"url": "https://www.pearltalent.com/resources/admin-assistant-job", "title": "What is an Admin Assistant: Job Description + 5 Benefits", "metadescription": "Explore the essential role of an admin assistant in modern workplaces, their responsibilities, and the benefits they bring to organizational efficiency.", "h1": "What is an Admin Assistant: Job Description + 5 Benefits"},
    {"url": "https://www.pearltalent.com/resources/outsourcing-strategy", "title": "Build Your Outsourcing Strategy in 5 Simple Steps + Examples", "metadescription": "A great outsourcing strategy gives you a way out of ineffective sticky situations by cutting costs, increasing efficiency, and accomplishing specialized tasks. But there are certain preliminaries you should follow – internal readiness assessments to ensure that it will benefit your organization in many ways.", "h1": "How To Build An Outsourcing Strategy In 5 Steps + Examples"},
    {"url": "https://www.pearltalent.com/resources/how-do-staffing-agencies-make-money", "title": "The Business Behind It: How Do Staffing Agencies Make Money", "metadescription": "Several businesses increasingly rely on staffing agencies to efficiently connect them with qualified candidates in a competitive job market. These agencies have become essential partners by managing the complexities of recruitment and placement, ensuring a good fit for both companies and job seekers.", "h1": "The Business Behind It: How Do Staffing Agencies Make Money"},
    
    # Batch 3 (URLs 23-33) - NEW BATCH
    {"url": "https://www.pearltalent.com/resources/what-is-a-medical-transcriptionist-job-description-for-2024", "title": "What is a Medical Transcriptionist: Job Description for 2024", "metadescription": "In the healthcare industry, the role of a medical transcriptionist is crucial. These professionals are entrusted with converting spoken medical records, reports, and dictations into written documents. Their precision and attention to detail are essential for ensuring healthcare documentation integrity.", "h1": "What is a Medical Transcriptionist: Job Description for 2024"},
    {"url": "https://www.pearltalent.com/resources/talent-acquisition-partner", "title": "Talent Acquisition Partner vs. Recruiter: Key Differences", "metadescription": "Today's job market is more competitive than ever, with organizations striving to attract and retain top talent. The talent acquisition partner and recruiter are both central to these efforts, each filling different roles and providing unique advantages in the hiring process. Understanding their differences is crucial for businesses looking to build effective recruitment strategies that serve their long-term business goals.", "h1": "Talent Acquisition Partner vs. Recruiter: Key Differences"},
    {"url": "https://www.pearltalent.com/resources/inbound-sales-representative", "title": "What Is an Inbound Sales Representative? A Comprehensive Overview", "metadescription": "A business's sales department is crucial for driving revenue and fostering growth. It involves various strategies to convert prospects into customers, from reaching out proactively to handling incoming inquiries. Understanding the different sales roles and their functions can enhance overall sales effectiveness.", "h1": "What Is an Inbound Sales Representative? A Comprehensive Overview"},
    {"url": "https://www.pearltalent.com/resources/offshore-outsourcing-examples", "title": "5+ Successful Offshore Outsourcing Examples and Strategies", "metadescription": "Discover successful offshore outsourcing examples and strategies to enhance your business operations and efficiency. Learn how to effectively implement outsourcing for your company.", "h1": "5+ Successful Offshore Outsourcing Examples and Strategies"},
    {"url": "https://www.pearltalent.com/resources/tasks-you-can-outsource-to-vas", "title": "133 Tasks You Can Outsource To A Virtual Assistant", "metadescription": "When you choose to outsource your tasks to a virtual assistant, you're not just getting an extra pair of hands; you're making a strategic investment in your business's success. Your time as a business owner is valuable and it's best spent on tasks that truly require your expertise.", "h1": "133 Tasks You Can Outsource To A Virtual Assistant"},
    {"url": "https://www.pearltalent.com/resources/remote-staffing-agency", "title": "11 Best Staffing Agencies in 2025 | Pearl Talent", "metadescription": "Explore the 11 best staffing agencies in 2025 that can help your business scale and find the right talent efficiently. Discover diverse specializations and service models to align with your hiring needs.", "h1": "11 of the The Best Staffing Agencies in 2025"},
    {"url": "https://www.pearltalent.com/resources/finance-and-accounting-outsourcing-companies", "title": "Top 11+ Finance and Accounting Outsourcing Companies", "metadescription": "Explore the leading finance and accounting outsourcing companies that can help your business improve efficiency and save money. Discover top service providers and their unique offerings.", "h1": "Top 11+ Finance and Accounting Outsourcing Companies"},
    {"url": "https://www.pearltalent.com/resources/revenue-cycle-management-companies", "title": "Top 10 Revenue Cycle Management Companies for Specialty Practices", "metadescription": "Choosing the right healthcare revenue cycle management company can make a significant difference in the financial health of your specialty practice. With the right partner, you can streamline your operations and ensure faster payments, reducing administrative burdens.", "h1": "Top 10 Revenue Cycle Management Companies for Specialty Practices"},
    {"url": "https://www.pearltalent.com/resources/best-virtual-assistant-websites", "title": "9+ Best Virtual Assistant Websites: Industry Insights", "metadescription": "Discover the best virtual assistant websites to help you find skilled professionals for various services, from administrative tasks to digital marketing. Explore platforms, pricing plans, and features to make an informed decision.", "h1": "9+ Best Virtual Assistant Websites: Industry Insights"},
    {"url": "https://www.pearltalent.com/resources/7-best-sites-to-hire-a-real-estate-virtual-assistant", "title": "7+ Best Sites to Hire A Real Estate Virtual Assistant", "metadescription": "Hiring a real estate virtual assistant offers a transformative solution for real estate professionals looking to optimize their operations. Whether you're a busy realtor juggling multiple clients or looking to free up some time, a virtual assistant can help to ease your workload.", "h1": "7+ Best Sites to Hire A Real Estate Virtual Assistant"}
]

def create_comprehensive_seo_analysis():
    """Create comprehensive CSV file with all scraped SEO data and advanced analytics."""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"pearl_talent_comprehensive_seo_analysis_{timestamp}.csv"
    
    headers = [
        'URL', 'Title', 'Meta Description', 'H1', 
        'Title Length', 'Meta Description Length', 'H1 Length', 
        'Title = H1?', 'SEO Issues', 'Page Category', 'Content Type'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for item in scraped_data:
            # Calculate metrics
            title_length = len(item['title'])
            meta_length = len(item['metadescription'])
            h1_length = len(item['h1'])
            title_equals_h1 = "Yes" if item['title'] == item['h1'] else "No"
            
            # Categorize content
            url_path = item['url'].split('/')[-1]
            if 'virtual-assistant' in url_path or 'va' in url_path:
                category = "Virtual Assistant"
            elif 'executive-assistant' in url_path or 'admin' in url_path:
                category = "Administrative"
            elif 'outsourcing' in url_path or 'outsource' in url_path:
                category = "Outsourcing"
            elif 'medical' in url_path or 'healthcare' in url_path:
                category = "Healthcare"
            elif 'sales' in url_path or 'finance' in url_path or 'accounting' in url_path:
                category = "Business Functions"
            elif 'staffing' in url_path or 'recruitment' in url_path or 'talent' in url_path:
                category = "Staffing & Recruitment"
            else:
                category = "General"
            
            # Determine content type
            if 'job-description' in url_path:
                content_type = "Job Description"
            elif 'sites' in url_path or 'companies' in url_path or 'websites' in url_path:
                content_type = "Directory/List"
            elif 'review' in url_path:
                content_type = "Review"
            elif 'cost' in url_path or 'statistics' in url_path:
                content_type = "Statistics/Pricing"
            elif 'skills' in url_path or 'role' in url_path:
                content_type = "Guide/Skills"
            else:
                content_type = "Guide/How-to"
            
            # SEO Issues
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
                item['url'], item['title'], item['metadescription'], item['h1'],
                title_length, meta_length, h1_length, title_equals_h1,
                seo_issues, category, content_type
            ])
    
    # Analytics
    total_urls = len(scraped_data)
    title_h1_matches = sum(1 for item in scraped_data if item['title'] == item['h1'])
    title_h1_mismatches = total_urls - title_h1_matches
    
    print(f"🎯 COMPREHENSIVE PEARL TALENT SEO ANALYSIS")
    print("=" * 80)
    print(f"✅ Created file: {filename}")
    print(f"📊 Total URLs analyzed: {total_urls}/74 ({total_urls/74*100:.1f}%)")
    print(f"🚀 Progress this session: +11 URLs ({total_urls-22} added)")
    
    # Enhanced metrics
    avg_title = sum(len(item['title']) for item in scraped_data) / total_urls
    avg_meta = sum(len(item['metadescription']) for item in scraped_data) / total_urls
    avg_h1 = sum(len(item['h1']) for item in scraped_data) / total_urls
    
    print(f"\n📏 CONTENT LENGTH ANALYSIS:")
    print("-" * 50)
    print(f"Average Title Length: {avg_title:.1f} chars")
    print(f"Average Meta Description: {avg_meta:.1f} chars")
    print(f"Average H1 Length: {avg_h1:.1f} chars")
    
    print(f"\n🎯 SEO COMPLIANCE ANALYSIS:")
    print("-" * 50)
    
    # Detailed issue breakdown
    long_titles = [item for item in scraped_data if len(item['title']) > 60]
    short_metas = [item for item in scraped_data if len(item['metadescription']) < 120]
    long_metas = [item for item in scraped_data if len(item['metadescription']) > 160]
    
    print(f"✅ Title/H1 Consistency: {title_h1_matches}/{total_urls} ({title_h1_matches/total_urls*100:.1f}%)")
    print(f"⚠️  Long Titles (>60): {len(long_titles)}/{total_urls} ({len(long_titles)/total_urls*100:.1f}%)")
    print(f"⚠️  Long Meta Desc (>160): {len(long_metas)}/{total_urls} ({len(long_metas)/total_urls*100:.1f}%)")
    print(f"⚠️  Short Meta Desc (<120): {len(short_metas)}/{total_urls} ({len(short_metas)/total_urls*100:.1f}%)")
    
    # Category breakdown
    categories = {}
    content_types = {}
    
    for item in scraped_data:
        url_path = item['url'].split('/')[-1]
        
        # Categorize
        if 'virtual-assistant' in url_path or 'va' in url_path:
            cat = "Virtual Assistant"
        elif 'executive-assistant' in url_path or 'admin' in url_path:
            cat = "Administrative"
        elif 'outsourcing' in url_path or 'outsource' in url_path:
            cat = "Outsourcing"
        elif 'medical' in url_path or 'healthcare' in url_path:
            cat = "Healthcare"
        elif 'sales' in url_path or 'finance' in url_path or 'accounting' in url_path:
            cat = "Business Functions"
        elif 'staffing' in url_path or 'recruitment' in url_path or 'talent' in url_path:
            cat = "Staffing & Recruitment"
        else:
            cat = "General"
        
        categories[cat] = categories.get(cat, 0) + 1
        
        # Content type
        if 'job-description' in url_path:
            ct = "Job Description"
        elif 'sites' in url_path or 'companies' in url_path or 'websites' in url_path:
            ct = "Directory/List"
        elif 'review' in url_path:
            ct = "Review"
        elif 'cost' in url_path or 'statistics' in url_path:
            ct = "Statistics/Pricing"
        elif 'skills' in url_path or 'role' in url_path:
            ct = "Guide/Skills"
        else:
            ct = "Guide/How-to"
        
        content_types[ct] = content_types.get(ct, 0) + 1
    
    print(f"\n📁 CONTENT CATEGORY BREAKDOWN:")
    print("-" * 50)
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: {count} pages ({count/total_urls*100:.1f}%)")
    
    print(f"\n📄 CONTENT TYPE BREAKDOWN:")
    print("-" * 50)
    for content_type, count in sorted(content_types.items(), key=lambda x: x[1], reverse=True):
        print(f"{content_type}: {count} pages ({count/total_urls*100:.1f}%)")
    
    # Title/H1 mismatches details
    if title_h1_mismatches > 0:
        mismatched_pages = [item for item in scraped_data if item['title'] != item['h1']]
        print(f"\n❌ TITLE/H1 MISMATCHES ({title_h1_mismatches} pages):")
        print("-" * 50)
        for item in mismatched_pages:
            page_name = item['url'].split('/')[-1]
            print(f"• {page_name}")
    
    print(f"\n🎯 NEXT STEPS:")
    print("-" * 50)
    print(f"📈 Progress: {total_urls}/74 URLs complete ({41-total_urls} remaining)")
    print(f"🔄 Continue scraping: {round((74-total_urls)/10)} more batches needed")
    print(f"🎯 ETA: ~{74-total_urls} more URLs to reach 100% coverage")
    
    return filename

if __name__ == "__main__":
    create_comprehensive_seo_analysis() 