# TERMIUM SCRAPER

This Python script, `search_termium.py`, is designed to perform automated searches on the Termium Plus website (https://www.btb.termiumplus.gc.ca/tpv2alpha/alpha-fra.html?lang=fra) using the Playwright library, specifically targeting the Chromium browser. It allows you to search for a specific query term on the website and extract information from the search results, particularly English and French records, along with their respective context.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:

1. Python: Ensure you have Python 3.7 or higher installed on your system.
2. Playwright: You need to have the Playwright library installed. You can install it using pip:

   ```
   pip install playwright
   ```

3. Chromium: This script uses Chromium as the browser. Playwright will automatically download Chromium for you.

## Usage

To use the `search_termium.py` script, follow these steps:

1. Import the necessary modules at the beginning of your Python script:

   ```python
   import asyncio
   from playwright.async_api import async_playwright
   from search_termium import search_termium
   ```

2. Create an asynchronous function to call `search_termium` and pass your desired search query:

   ```python
   async def main():
       query_string = "your_search_query_here"
       results = await search_termium(query_string)
       # Process and use the 'results' data as needed.
       print(results)  # You can modify this to suit your needs.
   ```

3. Run the event loop to execute the search and data extraction:

   ```python
   if __name__ == '__main__':
       loop = asyncio.get_event_loop()
       loop.run_until_complete(main())
   ```

4. Replace `"your_search_query_here"` with the actual search term you want to look up on Termium Plus.

5. Run your Python script, and it will perform the search and extract information from the Termium Plus website.

## Functionality

The script performs the following steps:

1. Launches a Chromium browser.
2. Navigates to the Termium Plus website.
3. Enters the search query into the search input field.
4. Clicks the search button.
5. Waits for search results to load.
6. Extracts information from each search result, including English and French records and their context.
7. Closes the browser and returns the results as a list of dictionaries.

You can further customize the script to suit your specific needs, such as processing or displaying the extracted data differently.
