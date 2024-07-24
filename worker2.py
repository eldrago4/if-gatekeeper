import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://ifatc.org/gates?code=vidp'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table
    table = soup.find('table')

    # Extract table rows
    rows = table.find_all('tr')

    # Extract and print data for the first few rows for demonstration
    extracted_data = []
    for row in rows[:5]:  # Limiting to first 5 rows for sample output
        cells = row.find_all('td')
        data = [cell.text.strip() for cell in cells]
        extracted_data.append(data)

    for data in extracted_data:
        print(data)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
