#!/usr/bin/env python3
"""
Merge Duplicate Talent Files
Consolidates duplicate talent profiles, keeping the more detailed versions
"""

import os
import shutil
from pathlib import Path

def merge_talent_files():
    """Merge duplicate talent files, keeping the detailed versions"""
    
    talent_dir = Path("Knowledge Base/07-talent")
    nested_talent_dir = talent_dir / "talent"
    
    if not nested_talent_dir.exists():
        print("❌ Nested talent directory not found")
        return
    
    print("🔄 Merging duplicate talent files...")
    
    merged_count = 0
    
    # Get all files from nested directory
    for nested_file in nested_talent_dir.glob("*.md"):
        direct_file = talent_dir / nested_file.name
        
        if direct_file.exists():
            # Compare file sizes to determine which has more content
            nested_size = nested_file.stat().st_size
            direct_size = direct_file.stat().st_size
            
            print(f"   📝 Processing {nested_file.name}...")
            print(f"      Nested version: {nested_size} bytes")
            print(f"      Direct version: {direct_size} bytes")
            
            # Keep the larger (more detailed) version
            if nested_size > direct_size:
                print(f"      ✅ Keeping nested version (more detailed)")
                # Remove the smaller direct version
                direct_file.unlink()
                # Move nested version to direct location
                shutil.move(str(nested_file), str(direct_file))
            else:
                print(f"      ✅ Keeping direct version (more detailed)")
                # Remove the smaller nested version
                nested_file.unlink()
            
            merged_count += 1
        else:
            # No duplicate, just move the nested file up
            print(f"   📝 Moving {nested_file.name} (no duplicate)")
            shutil.move(str(nested_file), str(direct_file))
            merged_count += 1
    
    # Remove empty nested directory
    if nested_talent_dir.exists() and not any(nested_talent_dir.iterdir()):
        nested_talent_dir.rmdir()
        print(f"   🗑️  Removed empty nested directory")
    
    print(f"\n✅ Merged {merged_count} talent files")
    print("🎯 Kept the most detailed versions of each profile")

if __name__ == "__main__":
    merge_talent_files() 