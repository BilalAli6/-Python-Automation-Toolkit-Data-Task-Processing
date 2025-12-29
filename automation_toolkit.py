#!/usr/bin/env python3
"""
Python Automation Toolkit
- Organize files by type
- Process CSV/JSON data
- Optional web scraping
Author: Muhammad Bilal Ali Saif
"""

import os
import shutil
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

# ----------------------------
# 1. File Organization
# ----------------------------
def organize_files(folder_path):
    """
    Organize files into folders based on file extension
    """
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            folder_name = os.path.join(folder_path, ext)
            os.makedirs(folder_name, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_name, filename))
    print(f"Files in '{folder_path}' organized by extension.\n")

# ----------------------------
# 2. CSV/JSON Processing
# ----------------------------
def process_csv(file_path, output_file=None):
    """
    Read CSV, perform simple summary, save as CSV/JSON
    """
    if not os.path.exists(file_path):
        print(f"CSV file '{file_path}' not found!")
        return

    df = pd.read_csv(file_path)
    print("CSV Summary:\n", df.describe())
    
    if output_file:
        ext = output_file.split('.')[-1].lower()
        if ext == 'csv':
            df.to_csv(output_file, index=False)
        elif ext == 'json':
            df.to_json(output_file, orient='records', indent=4)
        print(f"Processed data saved to {output_file}\n")

# ----------------------------
# 3. Web Scraping Example
# ----------------------------
def scrape_website(url, selector='p'):
    """
    Scrape a website and print selected elements (default: paragraphs)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.select(selector)
        for i, elem in enumerate(elements[:10], start=1):  # show top 10
            print(f"{i}. {elem.get_text(strip=True)}")
        print(f"\nScraping completed from {url}\n")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# ----------------------------
# 4. Main Menu
# ----------------------------
def main():
    while True:
        print("\n=== Python Automation Toolkit ===")
        print("1. Organize files")
        print("2. Process CSV/JSON file")
        print("3. Web scraping")
        print("4. Exit")

        choice = input("Enter choice [1-4]: ")
        if choice == '1':
            folder = input("Enter folder path to organize: ").strip()
            organize_files(folder)
        elif choice == '2':
            file_path = input("Enter CSV file path: ").strip()
            output_file = input("Enter output file (CSV/JSON) or leave blank: ").strip()
            output_file = output_file if output_file else None
            process_csv(file_path, output_file)
        elif choice == '3':
            url = input("Enter website URL to scrape: ").strip()
            selector = input("Enter CSS selector (default 'p'): ").strip() or 'p'
            scrape_website(url, selector)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
