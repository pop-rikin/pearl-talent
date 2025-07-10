#!/usr/bin/env python3
"""
Competitive Intelligence Pipeline
Uses Firecrawl + OpenAI/Claude to analyze competitors and identify gaps/opportunities
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any
import openai
from dataclasses import dataclass

@dataclass
class CompetitorData:
    name: str
    url: str
    content: str
    pricing: str
    positioning: str
    target_market: str
    scraped_at: datetime

class CompetitiveIntelligence:
    def __init__(self):
        self.competitors = {
            "upwork": {
                "name": "Upwork",
                "urls": [
                    "https://www.upwork.com/enterprise",
                    "https://www.upwork.com/pricing",
                    "https://www.upwork.com/about"
                ]
            },
            "toptal": {
                "name": "Toptal", 
                "urls": [
                    "https://www.toptal.com",
                    "https://www.toptal.com/pricing",
                    "https://www.toptal.com/about"
                ]
            },
            "turing": {
                "name": "Turing",
                "urls": [
                    "https://www.turing.com",
                    "https://www.turing.com/pricing",
                    "https://www.turing.com/about"
                ]
            },
            "gun_io": {
                "name": "Gun.io",
                "urls": [
                    "https://gun.io",
                    "https://gun.io/pricing"
                ]
            },
            "remote_team": {
                "name": "RemoteTeam",
                "urls": [
                    "https://www.remoteteam.com",
                    "https://www.remoteteam.com/pricing"
                ]
            }
        }
        
        # Pearl Talent's current positioning for comparison
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

    def scrape_competitor_content(self, competitor_key: str) -> CompetitorData:
        """
        Scrape competitor content using Firecrawl MCP
        In practice, this would call the Firecrawl MCP
        """
        competitor = self.competitors[competitor_key]
        
        # This would be replaced with actual Firecrawl MCP calls
        # For now, simulating the structure
        scraped_content = {
            "homepage": "Competitor homepage content...",
            "pricing": "Competitor pricing information...", 
            "about": "Competitor about/positioning content..."
        }
        
        return CompetitorData(
            name=competitor["name"],
            url=competitor["urls"][0],
            content=json.dumps(scraped_content),
            pricing="",
            positioning="",
            target_market="",
            scraped_at=datetime.now()
        )

    def analyze_competitor_gaps(self, competitor_data: CompetitorData) -> Dict[str, Any]:
        """
        Use OpenAI/Claude to analyze competitor content and identify gaps/opportunities
        """
        
        analysis_prompt = f"""
        You are a competitive intelligence analyst for Pearl Talent, a premium global talent acquisition company.

        PEARL TALENT'S POSITIONING:
        - Value Prop: {self.pearl_positioning['value_prop']}
        - Pricing: {self.pearl_positioning['pricing']}
        - Differentiators: {', '.join(self.pearl_positioning['differentiators'])}
        - Target Market: {self.pearl_positioning['target_market']}
        - Geographic Focus: {self.pearl_positioning['geographic_focus']}

        COMPETITOR DATA TO ANALYZE:
        Company: {competitor_data.name}
        Content: {competitor_data.content}

        Please analyze this competitor and provide:

        1. POSITIONING GAPS (what they're missing that Pearl could emphasize):
        - Service gaps
        - Market positioning weaknesses
        - Value proposition holes

        2. OPPORTUNITIES FOR PEARL:
        - Messaging opportunities
        - Market segments they're not serving well
        - Pricing positioning opportunities
        - Geographic advantages

        3. COMPETITIVE THREATS:
        - What they do better than Pearl
        - Potential competitive responses needed
        - Market positioning strengths

        4. ACTIONABLE RECOMMENDATIONS:
        - Specific messaging updates for Pearl
        - Pricing strategy adjustments
        - Market positioning improvements
        - Content/marketing opportunities

        Format your response as structured JSON with these exact keys:
        {
            "positioning_gaps": [],
            "opportunities": [],
            "threats": [],
            "recommendations": []
        }
        """

        try:
            # This would use the actual OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert competitive intelligence analyst."},
                    {"role": "user", "content": analysis_prompt}
                ],
                temperature=0.3
            )
            
            analysis = json.loads(response.choices[0].message.content)
            return analysis
            
        except Exception as e:
            print(f"Error in AI analysis: {e}")
            return {
                "positioning_gaps": ["Analysis failed"],
                "opportunities": ["Analysis failed"], 
                "threats": ["Analysis failed"],
                "recommendations": ["Analysis failed"]
            }

    def update_knowledge_base(self, competitor_name: str, analysis: Dict[str, Any]):
        """
        Update knowledge base files with competitive intelligence
        """
        
        # Update vs-competitor file
        competitor_file_content = f"""# Pearl Talent vs {competitor_name}

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Competitive Analysis Summary

### {competitor_name}'s Positioning Gaps
{chr(10).join(f"- {gap}" for gap in analysis['positioning_gaps'])}

### Opportunities for Pearl Talent
{chr(10).join(f"- {opp}" for opp in analysis['opportunities'])}

### Competitive Threats to Monitor
{chr(10).join(f"- {threat}" for threat in analysis['threats'])}

### Actionable Recommendations
{chr(10).join(f"- {rec}" for rec in analysis['recommendations'])}

## Pearl Talent's Competitive Advantages

### What We Do Better
- **Premium Quality Focus**: Top 1% talent vs. mixed quality platforms
- **White-Glove Service**: Managed services vs. self-service platforms  
- **Exclusive Networks**: University partnerships vs. public job boards
- **Founder Credibility**: Immigrant founders who built this themselves
- **Geographic Expertise**: Deep networks in Philippines, LatAm, South Africa

### Pricing Positioning
- **Pearl**: ${self.pearl_positioning['pricing']}
- **Value Justification**: Premium pricing reflects quality and ongoing support
- **ROI Focus**: $12K-$62K annual savings demonstrated across clients

### Target Market Differentiation
- **Pearl Focus**: Fast-scaling startups, unicorns, $100M+ funded companies
- **Service Model**: Partnership approach vs. transactional hiring
- **Success Metrics**: 90%+ retention rate, 90-day guarantee

## Recommended Messaging Against {competitor_name}

### Key Differentiators to Emphasize
1. **Quality Over Quantity**: "While {competitor_name} offers access to many freelancers, Pearl provides access to the top 1% of global talent through exclusive university partnerships."

2. **Managed Service vs. Platform**: "Unlike {competitor_name}'s self-service platform, Pearl provides white-glove managed services with ongoing support."

3. **Long-term Partnership**: "Pearl focuses on long-term career growth for talent and sustainable scaling for companies, not gig work."

### Objection Handling
**"Why not just use {competitor_name}?"**
- "Great question. {competitor_name} is excellent for project-based work, but Pearl specializes in finding exceptional full-time team members who become core parts of your company. Our 90%+ retention rate and 90-day guarantee reflect that difference."

## Competitive Intelligence Updates
*This section automatically updates based on ongoing monitoring*

### Recent Changes Detected
- [Auto-populated based on content changes]

### Market Positioning Shifts  
- [Auto-populated based on messaging analysis]

### Pricing Updates
- [Auto-populated based on pricing page changes]
"""

        return competitor_file_content

    def generate_overall_competitive_strategy(self, all_analyses: List[Dict[str, Any]]) -> str:
        """
        Use AI to synthesize insights across all competitors into overall strategy
        """
        
        strategy_prompt = f"""
        Based on competitive analysis of multiple competitors, generate an overall competitive strategy for Pearl Talent.

        COMPETITOR ANALYSES:
        {json.dumps(all_analyses, indent=2)}

        PEARL'S CURRENT POSITIONING:
        {json.dumps(self.pearl_positioning, indent=2)}

        Please provide:

        1. OVERALL MARKET POSITIONING STRATEGY
        2. KEY MESSAGING PILLARS TO EMPHASIZE  
        3. PRICING STRATEGY RECOMMENDATIONS
        4. MARKET OPPORTUNITIES TO PURSUE
        5. COMPETITIVE THREATS TO ADDRESS
        6. CONTENT/MARKETING STRATEGY UPDATES

        Format as markdown for direct inclusion in knowledge base.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a strategic marketing consultant specializing in competitive positioning."},
                    {"role": "user", "content": strategy_prompt}
                ],
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generating strategy: {e}"

    def run_full_analysis(self):
        """
        Run complete competitive intelligence pipeline
        """
        print("🕷️ Starting competitive intelligence analysis...")
        
        all_analyses = []
        
        for competitor_key in self.competitors.keys():
            print(f"📊 Analyzing {self.competitors[competitor_key]['name']}...")
            
            # Step 1: Scrape competitor content
            competitor_data = self.scrape_competitor_content(competitor_key)
            
            # Step 2: AI analysis for gaps/opportunities
            analysis = self.analyze_competitor_gaps(competitor_data)
            all_analyses.append({
                "competitor": competitor_data.name,
                "analysis": analysis
            })
            
            # Step 3: Update knowledge base
            kb_content = self.update_knowledge_base(competitor_data.name, analysis)
            
            # Save to knowledge base file
            filename = f"Knowledge Base/03-competitors/vs-{competitor_key.replace('_', '-')}.md"
            with open(filename, 'w') as f:
                f.write(kb_content)
            
            print(f"✅ Updated {filename}")
        
        # Step 4: Generate overall competitive strategy
        print("🎯 Generating overall competitive strategy...")
        overall_strategy = self.generate_overall_competitive_strategy(all_analyses)
        
        with open("Knowledge Base/03-competitors/competitive-strategy.md", 'w') as f:
            f.write(f"# Pearl Talent Competitive Strategy\n\n{overall_strategy}")
        
        print("✅ Competitive intelligence analysis complete!")
        return all_analyses

if __name__ == "__main__":
    # Example usage
    ci = CompetitiveIntelligence()
    ci.run_full_analysis() 