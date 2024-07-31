# Import necessary modules
from bs4 import BeautifulSoup
import requests

# Function to fetch and clean content from a URL
def fetch_and_clean(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Clean the content by removing HTML tags
            clean_content = remove_tags(response.content)
            return clean_content
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching content from {url}: {str(e)}")
        return None

# Function to remove HTML tags from content
def remove_tags(html):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Remove style and script elements
    for data in soup(['style', 'script']):
        data.decompose()
    
    # Return the cleaned content as a single string
    return ' '.join(soup.stripped_strings)

# List of URLs to scrape
urls = [
    'https://explitia.com/esg-strategy-in-a-manufacturing-company/',
    'https://incit.org/en/thought-leadership/optimising-capital-allocation-for-esg-key-strategies-for-manufacturers/',
    'https://www.forbes.com/sites/lisacaldwell/2023/03/29/suppliers-are-the-secret-sauce-to-manufacturers-esg-success/',
    'https://sustainabilitymag.com/top10/top-10'
]

# Variable to store aggregated data
aggregated_data = ""

# Iterate over the list of URLs and fetch and clean content
for url in urls:
    cleaned_content = fetch_and_clean(url)
    if cleaned_content:
        aggregated_data += cleaned_content + " "

# Save the aggregated data to a text file
with open("scraped_data.txt", "w") as file:
    file.write(aggregated_data)
