# Raw Data Directory

This directory stores raw outputs from various data collection tools and sources.

## Structure

- `firecrawl/` - Raw outputs from Firecrawl MCP scraping
- `competitive/` - Raw competitor data and analysis
- `talent/` - Raw talent profile data
- `website/` - Raw website content and structure data

## Data Sources

### Firecrawl MCP
- **Purpose**: Web scraping and content extraction
- **Output Format**: JSON and Markdown
- **Storage**: Timestamped files with source URL metadata

### Competitive Intelligence
- **Purpose**: Competitor website analysis
- **Output Format**: JSON analysis reports
- **Storage**: Organized by competitor and date

## Usage Guidelines

1. **Never edit raw data files** - these are source records
2. **Use timestamps** in filenames for version control
3. **Include metadata** about source, date, and collection method
4. **Reference raw files** in processed Knowledge Base content

## File Naming Convention

```
YYYY-MM-DD_source_type_description.json
YYYY-MM-DD_source_type_description.md
```

Examples:
- `2024-06-24_firecrawl_pearltalent_homepage.json`
- `2024-06-24_competitive_toptal_analysis.md` 