#!/usr/bin/env python3
"""
Data Exploration Script for Indigenous Wellbeing Analysis
This script helps explore and understand the available CSV datasets.
"""

import pandas as pd
import os
from pathlib import Path

def explore_data_files():
    """Explore all CSV files in the data directory."""
    data_dir = Path(__file__).parent / "data"
    
    print("🔍 EXPLORING INDIGENOUS WELLBEING DATASETS")
    print("=" * 60)
    
    # Get all CSV files
    csv_files = list(data_dir.glob("*.csv"))
    
    print(f"📊 Found {len(csv_files)} CSV files in the data directory\n")
    
    # Categorize files by type
    categories = {
        "Education & Culture": [],
        "Wellbeing & Mental Health": [],
        "Land Access": [],
        "Socioeconomic": [],
        "Other": []
    }
    
    for file in csv_files:
        filename = file.name
        if "Education" in filename or "culture" in filename.lower():
            categories["Education & Culture"].append(filename)
        elif "wellbeing" in filename.lower() or "mental" in filename.lower():
            categories["Wellbeing & Mental Health"].append(filename)
        elif "land" in filename.lower():
            categories["Land Access"].append(filename)
        elif "socioeconomic" in filename.lower() or "209-" in filename:
            categories["Socioeconomic"].append(filename)
        else:
            categories["Other"].append(filename)
    
    # Display categorized files
    for category, files in categories.items():
        if files:
            print(f"\n📁 {category} ({len(files)} files):")
            for file in sorted(files):
                print(f"   • {file}")
    
    # Show sample data from key files
    print("\n" + "=" * 60)
    print("📋 SAMPLE DATA PREVIEW")
    print("=" * 60)
    
    key_files = [
        "Education intentions and culture taught in school, 2008 and 2014-15_1.1 Survey_State.csv",
        "118-Social-emotional-wellbeing-Jan-23_D1.18.14.csv",
        "214-Indigenous-people-access-traditional-lands_D2.14.1.csv",
        "209-Socioeconomic-indexes-Aug-24_D2.09.1.csv"
    ]
    
    for filename in key_files:
        file_path = data_dir / filename
        if file_path.exists():
            print(f"\n📄 {filename}")
            print("-" * 40)
            try:
                df = pd.read_csv(file_path)
                print(f"Shape: {df.shape}")
                print(f"Columns: {list(df.columns)}")
                print("\nFirst 5 rows:")
                print(df.head())
                print("\n" + "=" * 60)
            except Exception as e:
                print(f"Error reading file: {e}")

def show_data_summary():
    """Show a summary of available data."""
    data_dir = Path(__file__).parent / "data"
    
    print("\n📈 DATA SUMMARY")
    print("=" * 60)
    
    # Count files by state/region
    state_files = {}
    for file in data_dir.glob("*.csv"):
        filename = file.name
        if "_NSW.csv" in filename:
            state_files["NSW"] = state_files.get("NSW", 0) + 1
        elif "_Vic.csv" in filename:
            state_files["Victoria"] = state_files.get("Victoria", 0) + 1
        elif "_Qld.csv" in filename:
            state_files["Queensland"] = state_files.get("Queensland", 0) + 1
        elif "_WA.csv" in filename:
            state_files["Western Australia"] = state_files.get("Western Australia", 0) + 1
        elif "_SA.csv" in filename:
            state_files["South Australia"] = state_files.get("South Australia", 0) + 1
        elif "_Tas.csv" in filename:
            state_files["Tasmania"] = state_files.get("Tasmania", 0) + 1
        elif "_NT.csv" in filename:
            state_files["Northern Territory"] = state_files.get("Northern Territory", 0) + 1
        elif "_ACT.csv" in filename:
            state_files["ACT"] = state_files.get("ACT", 0) + 1
    
    print("📊 Data by State/Territory:")
    for state, count in sorted(state_files.items()):
        print(f"   {state}: {count} files")
    
    print(f"\n🎯 Total datasets available: {len(list(data_dir.glob('*.csv')))}")
    print("✅ All data is now stored within the project directory!")

if __name__ == "__main__":
    explore_data_files()
    show_data_summary()
