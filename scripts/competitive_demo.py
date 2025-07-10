#!/usr/bin/env python3
"""
Competitive Intelligence Demo
Shows how to scrape competitor content and analyze for gaps/opportunities
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class CompetitiveDemo:
    def __init__(self):
        self.pearl_positioning = {
            "value_prop": "Access Remote Talent from Prestigious Companies and Top Universities",
            "pricing": "Managed Services: $3,000/month, Direct Placement: $7,500 one-time",
            "differentiators": [
                "Top 1% talent from exclusive networks",
                "White-glove managed services", 
                "90-day guarantee with free replacements",
                "Direct partnerships with universities",
                "Founder-led with immigrant experience",
                "Premium pricing reflecting quality"
            ],
            "target_market": "Fast-scaling companies, $100M+ funded startups, unicorns",
            "geographic_focus": "Philippines, Latin America, South Africa"
        }

    def create_analysis_prompt(self, competitor_name: str, competitor_content: str) -> str:
        """Create the AI analysis prompt"""
        return f"""
        You are a competitive intelligence analyst for Pearl Talent, a premium global talent acquisition company.

        PEARL TALENT'S POSITIONING:
        - Value Prop: {self.pearl_positioning['value_prop']}
        - Pricing: {self.pearl_positioning['pricing']}
        - Differentiators: {', '.join(self.pearl_positioning['differentiators'])}
        - Target Market: {self.pearl_positioning['target_market']}
        - Geographic Focus: {self.pearl_positioning['geographic_focus']}

        COMPETITOR DATA TO ANALYZE:
        Company: {competitor_name}
        Content: {competitor_content}

        Please analyze this competitor and identify:

        1. POSITIONING GAPS (what they're missing that Pearl could emphasize):
        - Service gaps they have
        - Market positioning weaknesses
        - Value proposition holes

        2. OPPORTUNITIES FOR PEARL:
        - Messaging opportunities we should pursue
        - Market segments they're not serving well
        - Pricing positioning advantages we have
        - Geographic advantages we can leverage

        3. COMPETITIVE THREATS:
        - What they do better than Pearl
        - Potential competitive responses we need
        - Their positioning strengths

        4. ACTIONABLE RECOMMENDATIONS:
        - Specific messaging updates for Pearl
        - Pricing strategy insights
        - Market positioning improvements
        - Content/marketing opportunities

        Please provide detailed, actionable insights based on the content provided.
        """

    def generate_competitor_analysis(self, competitor_name: str, analysis_results: Dict[str, List[str]]) -> str:
        """Generate formatted competitor analysis file"""
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return f"""# Pearl Talent vs {competitor_name}

*Last Updated: {current_time}*
*Analysis generated via AI-powered competitive intelligence*

## Executive Summary

This analysis examines {competitor_name}'s positioning, pricing, and market approach to identify strategic opportunities for Pearl Talent.

## Competitive Analysis Results

### {competitor_name}'s Positioning Gaps
{chr(10).join(f"- {gap}" for gap in analysis_results.get('positioning_gaps', []))}

### Strategic Opportunities for Pearl Talent
{chr(10).join(f"- {opp}" for opp in analysis_results.get('opportunities', []))}

### Competitive Threats to Monitor
{chr(10).join(f"- {threat}" for threat in analysis_results.get('threats', []))}

### Actionable Recommendations
{chr(10).join(f"- {rec}" for rec in analysis_results.get('recommendations', []))}

## Pearl Talent's Competitive Advantages

### What We Do Better
- **Premium Quality Focus**: Top 1% talent vs. mixed quality platforms
- **White-Glove Service**: Managed services vs. self-service platforms  
- **Exclusive Networks**: University partnerships vs. public job boards
- **Founder Credibility**: Immigrant founders who understand the talent journey
- **Geographic Expertise**: Deep networks in Philippines, LatAm, South Africa
- **Success Metrics**: 90%+ retention rate, 90-day guarantee

### Pricing Positioning
- **Pearl Pricing**: {self.pearl_positioning['pricing']}
- **Value Justification**: Premium pricing reflects quality and ongoing support
- **ROI Demonstration**: $12K-$62K annual savings proven across client base

### Target Market Differentiation
- **Pearl Focus**: Fast-scaling startups, unicorns, $100M+ funded companies
- **Service Model**: Partnership approach vs. transactional hiring
- **Long-term Commitment**: Career growth focus vs. gig work

## Recommended Messaging Against {competitor_name}

### Key Differentiators to Emphasize

**Quality Over Quantity**
> "While {competitor_name} offers access to many freelancers, Pearl provides access to the top 1% of global talent through exclusive university partnerships."

**Managed Service vs. Platform** 
> "Unlike {competitor_name}'s self-service platform, Pearl provides white-glove managed services with ongoing support throughout the entire talent lifecycle."

**Long-term Partnership**
> "Pearl focuses on building lasting career relationships and sustainable company scaling, not short-term gig work."

### Objection Handling Scripts

**"Why not just use {competitor_name}?"**
> "Excellent question. {competitor_name} is great for project-based work, but Pearl specializes in finding exceptional full-time team members who become integral parts of your company. Our 90%+ retention rate and 90-day guarantee demonstrate that difference in approach and outcomes."

**"Isn't Pearl more expensive?"**
> "Pearl's pricing reflects the premium quality and ongoing support we provide. When you factor in our clients' average savings of $12K-$62K annually, plus the reduced hiring and management overhead, Pearl typically delivers better ROI than platform-based solutions."

## Battle Card Summary

### When Competing Against {competitor_name}

**Lead With:**
- Quality and exclusivity of talent network
- White-glove managed service approach  
- Proven ROI and client success metrics
- Long-term partnership vs. transactional relationship

**Address Concerns About:**
- Premium pricing (emphasize ROI and value)
- Managed service vs. self-service (emphasize support benefits)
- Geographic focus (emphasize deep expertise in key markets)

**Avoid:**
- Direct price comparisons without context
- Disparaging their platform approach
- Over-promising on timeline or guarantees

## Competitive Intelligence Updates
*This section will auto-update as we monitor competitor changes*

### Recent Changes Detected
- [Auto-populated based on ongoing monitoring]

### Market Positioning Shifts  
- [Auto-populated based on messaging analysis]

### Pricing Updates
- [Auto-populated based on pricing page monitoring]

---

*This analysis was generated using AI-powered competitive intelligence. For the most current information, refer to the latest competitor monitoring reports.*
"""

    def save_analysis_to_kb(self, competitor_name: str, analysis_content: str):
        """Save analysis to knowledge base"""
        
        # Create safe filename
        safe_name = competitor_name.lower().replace(' ', '-').replace('.', '')
        filename = f"Knowledge Base/03-competitors/vs-{safe_name}.md"
        
        # Ensure directory exists
        os.makedirs("Knowledge Base/03-competitors", exist_ok=True)
        
        # Save file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(analysis_content)
        
        return filename

    def demo_analysis_workflow(self):
        """Demonstrate the complete competitive analysis workflow"""
        
        print("🎯 Pearl Talent Competitive Intelligence Demo")
        print("=" * 50)
        
        # Example: We'll demonstrate with a simulated competitor analysis
        competitor_name = "Upwork Enterprise"
        
        print(f"\n📊 Analyzing {competitor_name}...")
        
        # Step 1: Show what the Firecrawl scraping would look like
        print("\n🕷️ Step 1: Web Scraping (Firecrawl MCP)")
        print("   - Scraping homepage, pricing, and about pages")
        print("   - Extracting key messaging and positioning")
        print("   - Gathering pricing and service information")
        
        # Step 2: Show the AI analysis prompt
        print("\n🤖 Step 2: AI Analysis Prompt")
        sample_content = """
        Upwork Enterprise Content Summary:
        - Positioning: "The world's largest talent marketplace"
        - Pricing: Custom enterprise pricing, percentage-based fees
        - Target: Large enterprises needing flexible workforce
        - Service: Self-service platform with enterprise support
        - Geography: Global marketplace approach
        """
        
        analysis_prompt = self.create_analysis_prompt(competitor_name, sample_content)
        print("   Prompt created for AI analysis...")
        print(f"   Prompt length: {len(analysis_prompt)} characters")
        
        # Step 3: Simulate AI analysis results
        print("\n📈 Step 3: AI Analysis Results")
        sample_analysis = {
            "positioning_gaps": [
                "No focus on premium talent quality - treats all freelancers equally",
                "Self-service model lacks white-glove support for complex hires",
                "No exclusive talent networks or university partnerships",
                "Percentage-based pricing creates misaligned incentives",
                "Generic global approach lacks geographic specialization"
            ],
            "opportunities": [
                "Emphasize Pearl's top 1% talent vs. Upwork's open marketplace",
                "Highlight managed service benefits vs. self-service complexity", 
                "Leverage university partnerships as exclusive differentiator",
                "Position fixed pricing as more predictable than percentage fees",
                "Target companies frustrated with Upwork's quality inconsistency"
            ],
            "threats": [
                "Massive scale and brand recognition in freelance space",
                "Enterprise features and integrations already built",
                "Lower perceived cost for project-based work",
                "Established relationships with large enterprise clients"
            ],
            "recommendations": [
                "Create 'Upwork vs Pearl' comparison highlighting quality differences",
                "Develop case studies showing ROI of managed services",
                "Target Upwork enterprise customers with quality pain points",
                "Emphasize long-term hiring vs. project-based work positioning"
            ]
        }
        
        for category, items in sample_analysis.items():
            print(f"   {category.replace('_', ' ').title()}: {len(items)} insights")
        
        # Step 4: Generate knowledge base content
        print("\n📝 Step 4: Knowledge Base Update")
        analysis_content = self.generate_competitor_analysis(competitor_name, sample_analysis)
        
        # Step 5: Save to knowledge base
        filename = self.save_analysis_to_kb(competitor_name, analysis_content)
        print(f"   ✅ Saved analysis to: {filename}")
        
        # Step 6: Show what the ongoing monitoring would look like
        print("\n🔄 Step 5: Ongoing Monitoring Setup")
        print("   - Schedule weekly competitor page scraping")
        print("   - Monitor for pricing changes, new features, messaging updates")
        print("   - Auto-generate alerts for significant competitive shifts")
        print("   - Update battle cards and sales materials automatically")
        
        print(f"\n🎉 Demo Complete!")
        print(f"📁 Check the generated file: {filename}")
        
        return filename

if __name__ == "__main__":
    demo = CompetitiveDemo()
    result_file = demo.demo_analysis_workflow()
    print(f"\n📖 To see the full analysis, open: {result_file}") 