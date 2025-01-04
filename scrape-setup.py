# import necessary packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Basic scraping to get the page's title
# url = "https://en.wikipedia.org/wiki/Web_scraping"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     print(soup.title.string)  # Print the page title
# else:
#     print("Failed to fetch the page")

# web scraping function to scrape Parameswara's website
def scrape_table(url):
     # Send an HTTP request to the URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table with the specified classes
    table = soup.find('table', class_='infobox vcard')
    if not table:
        print("No table with class 'infobox vcard' found on the page.")
        return []

        # Initialize a list to store extracted data
    data = []

        # Find all tr tags within the tbody of the table
    tbody = table.find('tbody')
    if not tbody:
        print("No tbody found within the table.")
        return []

    rows = tbody.find_all('tr')
    for row in rows:
            # Find all td tags within the tr
        tds = row.find_all('td')
        for td in tds:
                # Extract and clean the text content
            text = td.get_text(strip=True)
            data.append(text)
    tabled = pd.DataFrame(data)
    return tabled


# Example usage
wikipedia_url = "https://en.wikipedia.org/wiki/Parameswara_of_Malacca"  # Replace with your desired URL
extracted_data = scrape_table(wikipedia_url)
print("Extracted Data:", extracted_data)



