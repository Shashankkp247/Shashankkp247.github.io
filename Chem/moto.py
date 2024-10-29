import requests
from bs4 import BeautifulSoup
import re

def extract_chapters_and_save_to_file(url):
    # Request the webpage content
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, timeout=10)

    response.raise_for_status()  # Check for successful response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a file name based on the domain and page title
    page_title = soup.title.string if soup.title else 'output'
    page_title_clean = re.sub(r'\W+', '_', page_title)  # Replace non-alphanumeric chars with underscores
    domain = re.sub(r'https?://(www\.)?', '', url).split('/')[0]
    file_name = f"{domain}_{page_title_clean}.txt"

    # Locate the first table
    table = soup.find('table')
    if not table:
        print("No table found on the page.")
        return

    # Open the file to save the data
    with open(file_name, 'w', encoding='utf-8') as file:
        # Extract chapter names and links
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 2:
                chapter_name = columns[0].get_text(strip=True)
                download_link = columns[1].find('a')['href'] if columns[1].find('a') else 'No link available'
                file.write(f"Chapter: {chapter_name}\nLink: {download_link}\n\n")

    print(f"Data saved to {file_name}")

# Get URL input from the user
url = 'https://jeemain.guru/pdf-download-motion-iitjee-chemistry-module-theory/'
extract_chapters_and_save_to_file(url)
