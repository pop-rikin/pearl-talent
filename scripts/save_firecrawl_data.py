#!/usr/bin/env python3
"""
Save Firecrawl Data
Automatically saves raw Firecrawl outputs with proper metadata and file structure
"""

import json
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

def save_firecrawl_data(url, content, format_type="markdown", tool_used="firecrawl_scrape", metadata=None):
    """
    Save raw Firecrawl data with proper metadata and file naming
    
    Args:
        url (str): Source URL that was scraped
        content (str): Raw content from Firecrawl
        format_type (str): Type of content (markdown, json, html)
        tool_used (str): Firecrawl tool used (scrape, crawl, search, etc.)
        metadata (dict): Additional metadata to include
    """
    
    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Parse URL for filename
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace('www.', '').replace('.', '_')
    path_part = parsed_url.path.replace('/', '_').replace('-', '_')
    if path_part == '_':
        path_part = 'homepage'
    
    # Create filename
    filename = f"{timestamp}_{domain}_{path_part}_{tool_used}"
    
    # Determine file extension
    if format_type.lower() in ['markdown', 'md']:
        ext = '.md'
    elif format_type.lower() == 'json':
        ext = '.json'
    else:
        ext = '.txt'
    
    # Create full file path
    raw_dir = Path("data/raw/firecrawl")
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    content_file = raw_dir / f"{filename}{ext}"
    metadata_file = raw_dir / f"{filename}_metadata.json"
    
    # Prepare metadata
    file_metadata = {
        "source_url": url,
        "scraped_at": datetime.now().isoformat(),
        "tool_used": tool_used,
        "format": format_type,
        "content_file": str(content_file.name),
        "domain": parsed_url.netloc,
        "path": parsed_url.path,
        "content_length": len(content),
        "custom_metadata": metadata or {}
    }
    
    # Save content file
    with open(content_file, 'w', encoding='utf-8') as f:
        if format_type.lower() == 'json' and isinstance(content, dict):
            json.dump(content, f, indent=2, ensure_ascii=False)
        else:
            f.write(content)
    
    # Save metadata file
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(file_metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved Firecrawl data:")
    print(f"   Content: {content_file}")
    print(f"   Metadata: {metadata_file}")
    print(f"   Source: {url}")
    print(f"   Size: {len(content):,} characters")
    
    return content_file, metadata_file

def save_firecrawl_batch(results, tool_used="firecrawl_batch"):
    """
    Save multiple Firecrawl results from batch operations
    
    Args:
        results (list): List of result dictionaries with 'url' and 'content' keys
        tool_used (str): Tool used for batch operation
    """
    
    saved_files = []
    
    for i, result in enumerate(results):
        url = result.get('url', f'unknown_url_{i}')
        content = result.get('content', '')
        metadata = {
            "batch_index": i,
            "batch_size": len(results),
            "batch_tool": tool_used
        }
        
        content_file, metadata_file = save_firecrawl_data(
            url=url,
            content=content,
            tool_used=tool_used,
            metadata=metadata
        )
        
        saved_files.append({
            "url": url,
            "content_file": content_file,
            "metadata_file": metadata_file
        })
    
    print(f"\n📦 Batch save complete: {len(saved_files)} files saved")
    return saved_files

def list_firecrawl_data():
    """List all saved Firecrawl data files"""
    
    raw_dir = Path("data/raw/firecrawl")
    
    if not raw_dir.exists():
        print("❌ No Firecrawl data directory found")
        return
    
    content_files = list(raw_dir.glob("*.md")) + list(raw_dir.glob("*.json")) + list(raw_dir.glob("*.txt"))
    content_files = [f for f in content_files if not f.name.endswith('_metadata.json')]
    
    if not content_files:
        print("📁 No Firecrawl data files found")
        return
    
    print(f"📊 Found {len(content_files)} Firecrawl data files:")
    
    for file_path in sorted(content_files):
        metadata_path = file_path.parent / f"{file_path.stem}_metadata.json"
        
        if metadata_path.exists():
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
            
            print(f"   📄 {file_path.name}")
            print(f"      URL: {metadata.get('source_url', 'Unknown')}")
            print(f"      Date: {metadata.get('scraped_at', 'Unknown')}")
            print(f"      Size: {metadata.get('content_length', 0):,} chars")
        else:
            print(f"   📄 {file_path.name} (no metadata)")

def create_data_index():
    """Create an index of all Firecrawl data for easy reference"""
    
    raw_dir = Path("data/raw/firecrawl")
    index_file = raw_dir / "data_index.json"
    
    if not raw_dir.exists():
        print("❌ No Firecrawl data directory found")
        return
    
    metadata_files = list(raw_dir.glob("*_metadata.json"))
    
    index_data = {
        "created_at": datetime.now().isoformat(),
        "total_files": len(metadata_files),
        "files": []
    }
    
    for metadata_file in sorted(metadata_files):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        index_data["files"].append({
            "content_file": metadata.get("content_file"),
            "metadata_file": metadata_file.name,
            "source_url": metadata.get("source_url"),
            "scraped_at": metadata.get("scraped_at"),
            "tool_used": metadata.get("tool_used"),
            "domain": metadata.get("domain"),
            "content_length": metadata.get("content_length")
        })
    
    with open(index_file, 'w') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Created data index: {index_file}")
    print(f"   Total files indexed: {len(metadata_files)}")

if __name__ == "__main__":
    print("🗂️  Firecrawl Data Management")
    print("Available commands:")
    print("  list_firecrawl_data() - List all saved data")
    print("  create_data_index() - Create searchable index")
    
    # Example usage:
    # save_firecrawl_data("https://example.com", "content here", "markdown") 