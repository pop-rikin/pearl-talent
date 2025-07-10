#!/usr/bin/env python3
"""
Script to scrape Pearl Talent resource pages and extract SEO data (title, meta description, H1)
Creates a CSV file with the extracted data.
"""

import csv
import json
import time
from datetime import datetime
from typing import List, Dict, Any

# List of URLs to scrape
URLS = [
    "https://www.pearltalent.com/resources/executive-assistant-to-ceo-job-description",
    "https://www.pearltalent.com/resources/executive-assistant-job-description",
    "https://www.pearltalent.com/resources/honest-review-of-taskus-a-2024-ultimate-guide",
    "https://www.pearltalent.com/resources/healthcare-virtual-assistant-hiring-platforms-7-sites",
    "https://www.pearltalent.com/resources/administrative-assistant-skills",
    "https://www.pearltalent.com/resources/hire-executive-assistant",
    "https://www.pearltalent.com/resources/types-of-outsourcing",
    "https://www.pearltalent.com/resources/7-sites-to-search-for-medical-virtual-assistant-jobs-in-2023",
    "https://www.pearltalent.com/resources/best-calendar-management-tools",
    "https://www.pearltalent.com/resources/client-success-manager-role",
    "https://www.pearltalent.com/resources/executive-assistant-job-description-examples-tips",
    "https://www.pearltalent.com/resources/virtual-assistant-cost",
    "https://www.pearltalent.com/resources/top-virtual-assistant-websites",
    "https://www.pearltalent.com/resources/personal-assistant-job-description",
    "https://www.pearltalent.com/resources/amazon-virtual-assistant-jobs",
    "https://www.pearltalent.com/resources/how-much-for-a-virtual-assistant-global-statistics-for-2023",
    "https://www.pearltalent.com/resources/remote-sales-representative",
    "https://www.pearltalent.com/resources/medical-billing-outsourcing-companies",
    "https://www.pearltalent.com/resources/bookkeeping-services-for-small-businesses",
    "https://www.pearltalent.com/resources/admin-assistant-job",
    "https://www.pearltalent.com/resources/outsourcing-strategy",
    "https://www.pearltalent.com/resources/how-do-staffing-agencies-make-money",
    "https://www.pearltalent.com/resources/what-is-a-medical-transcriptionist-job-description-for-2024",
    "https://www.pearltalent.com/resources/talent-acquisition-partner",
    "https://www.pearltalent.com/resources/inbound-sales-representative",
    "https://www.pearltalent.com/resources/offshore-outsourcing-examples",
    "https://www.pearltalent.com/resources/tasks-you-can-outsource-to-vas",
    "https://www.pearltalent.com/resources/remote-staffing-agency",
    "https://www.pearltalent.com/resources/finance-and-accounting-outsourcing-companies",
    "https://www.pearltalent.com/resources/revenue-cycle-management-companies",
    "https://www.pearltalent.com/resources/best-virtual-assistant-websites",
    "https://www.pearltalent.com/resources/7-best-sites-to-hire-a-real-estate-virtual-assistant",
    "https://www.pearltalent.com/resources/7-best-virtual-assistant-companies-to-source-talent-in-2024",
    "https://www.pearltalent.com/resources/customer-support-outsourcing",
    "https://www.pearltalent.com/resources/it-staffing-agencies",
    "https://www.pearltalent.com/resources/hire-administrative-assistant",
    "https://www.pearltalent.com/resources/top-7-customer-service-bpo-companies-to-watch-in-2024",
    "https://www.pearltalent.com/resources/healthcare-virtual-assistant",
    "https://www.pearltalent.com/resources/best-outsource-cpa-services-for-startup",
    "https://www.pearltalent.com/resources/top-it-staffing-companies-in-usa",
    "https://www.pearltalent.com/resources/legal-virtual-assistant",
    "https://www.pearltalent.com/resources/benefits-of-outsourcing-philippines",
    "https://www.pearltalent.com/resources/medical-appointment-scheduling-software",
    "https://www.pearltalent.com/resources/medical-transcription-software",
    "https://www.pearltalent.com/resources/how-do-temp-agencies-work",
    "https://www.pearltalent.com/resources/benefits-of-hiring-a-virtual-assistant",
    "https://www.pearltalent.com/resources/outsourced-sales-team",
    "https://www.pearltalent.com/resources/e-commerce-virtual-assistants",
    "https://www.pearltalent.com/resources/finance-staffing-agency",
    "https://www.pearltalent.com/resources/virtual-assistant-outsourcing-top-9-reasons-to-consider",
    "https://www.pearltalent.com/resources/how-to-hire-a-virtual-assistant-for-real-estate-agents",
    "https://www.pearltalent.com/resources/remote-bookkeeping",
    "https://www.pearltalent.com/resources/outsource-customer-service",
    "https://www.pearltalent.com/resources/virtual-assistant-philippines",
    "https://www.pearltalent.com/resources/executive-marketing-recruiters",
    "https://www.pearltalent.com/resources/top-rpo-companies",
    "https://www.pearltalent.com/resources/how-to-hire-the-best-virtual-assistant-for-small-business",
    "https://www.pearltalent.com/resources/outsource-healthcare",
    "https://www.pearltalent.com/resources/healthcare-virtual-assistant-companies",
    "https://www.pearltalent.com/resources/medical-business-process-outsourcing",
    "https://www.pearltalent.com/resources/virtual-executive-assistants-for-large-organizations",
    "https://www.pearltalent.com/resources/what-is-a-temp-agency",
    "https://www.pearltalent.com/resources/b2b-sales-outsourcing-companies",
    "https://www.pearltalent.com/resources/outsource-medical-billing",
    "https://www.pearltalent.com/resources/virtual-medical-receptionist",
    "https://www.pearltalent.com/resources/outsourcing-accounting-services-for-small-business",
    "https://www.pearltalent.com/resources/healthcare-business-process-outsourcing-services",
    "https://www.pearltalent.com/resources/outsource-web-design-philippines",
    "https://www.pearltalent.com/resources/nearshore-outsourcing",
    "https://www.pearltalent.com/resources/top-7-reasons-to-outsource-it-managed-services-2023-guide",
    "https://www.pearltalent.com/resources/what-is-talent-acquisition",
    "https://www.pearltalent.com/resources/payroll-outsourcing-service",
    "https://www.pearltalent.com/resources/seo-outsourcing-company",
    "https://www.pearltalent.com/resources/top-9-sites-to-outsource-seo-tasks-a-guide-for-2023"
]

def create_csv_with_manual_data():
    """
    Create CSV file with manually processed data.
    Since we need to use Firecrawl MCP interactively, this will create
    a template CSV and processing instructions.
    """
    
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"pearl_talent_seo_data_{timestamp}.csv"
    
    # CSV headers
    headers = ['URL', 'Title', 'Meta Description', 'H1', 'Status', 'Notes']
    
    # Create CSV file with headers and first row as example
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        # Add example row from our successful test
        writer.writerow([
            "https://www.pearltalent.com/resources/executive-assistant-to-ceo-job-description",
            "Comprehensive 2024 CEO Executive Assistant Job Description Template",
            "Providing a clear CEO executive assistant job description is essential to hiring a candidate who can give the CEO the most effective support. A well-crafted job description helps organizations attract qualified candidates who can contribute to the CEO's strategic goals and overall efficiency.",
            "Comprehensive 2024 CEO Executive Assistant Job Description Template",
            "SUCCESS",
            "Scraped successfully"
        ])
        
        # Add remaining URLs as placeholders
        for url in URLS[1:]:  # Skip first URL since we already have it
            writer.writerow([
                url,
                "", # Title - to be filled
                "", # Meta Description - to be filled  
                "", # H1 - to be filled
                "PENDING", # Status
                "Awaiting scrape"
            ])
    
    print(f"Created CSV template: {filename}")
    print(f"Total URLs to process: {len(URLS)}")
    return filename

def print_firecrawl_commands():
    """
    Print the Firecrawl MCP commands needed to process each URL.
    """
    print("\n" + "="*80)
    print("FIRECRAWL MCP COMMANDS TO RUN:")
    print("="*80)
    
    for i, url in enumerate(URLS, 1):
        print(f"\n# URL {i}/{len(URLS)}")
        print(f"# {url}")
        print("Use this Firecrawl command:")
        print(f'mcp_firecrawl-mcp_firecrawl_scrape')
        print(f'url: {url}')
        print('formats: ["extract"]')
        print('extract: {"prompt": "Extract the page title, meta description, and H1 heading from this webpage", "schema": {"type": "object", "properties": {"title": {"type": "string", "description": "The content of the <title> tag"}, "metadescription": {"type": "string", "description": "The content of the meta description tag"}, "h1": {"type": "string", "description": "The text content of the H1 heading tag"}, "url": {"type": "string", "description": "The URL of the page"}}, "required": ["title", "metadescription", "h1", "url"]}}')
        print("-" * 40)

if __name__ == "__main__":
    print("Pearl Talent SEO Data Scraper")
    print("="*50)
    
    # Create CSV template
    csv_filename = create_csv_with_manual_data()
    
    # Print commands for manual processing
    print_firecrawl_commands()
    
    print(f"\n✅ CSV template created: {csv_filename}")
    print("📝 Use the Firecrawl MCP commands above to scrape each URL")
    print("📊 Update the CSV file with the extracted data")
    
    print("\n🔄 Processing Summary:")
    print(f"Total URLs: {len(URLS)}")
    print(f"Completed: 1 (example)")
    print(f"Remaining: {len(URLS) - 1}") 