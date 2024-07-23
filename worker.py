
import requests
from bs4 import BeautifulSoup
import sqlite3

# List of ICAO codes
icao_codes = ["KATL", "ZBAA", "KLAX", "OMDB", "RJTT", "KORD", "EGLL", "ZSPD", "LFPG", "KDFW", "ZGGG", "EDDF", "LTFM", "EHAM", "VHHH", "WSSS", "RKSI", "KDEN", "VIDP", "VTBS"]

# Create a SQLite database named 'gates'
conn = sqlite3.connect('gates.db')
cursor = conn.cursor()

# Function to create table for each ICAO code

def create_table(icao):
    cursor.execute(f"DROP TABLE IF EXISTS {icao}")
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {icao} (
            name TEXT,

            type TEXT

        )
    ''')

# Function to insert data into the table

def insert_data(icao, name, type):
    cursor.execute(f'''
        INSERT INTO {icao} (name, type)
        VALUES (?, ?)
    ''', (name, type))
    conn.commit()

# Function to scrape data from the website
def scrape_data(icao):
    url = f'https://ifatc.org/gates?code={icao}'

    response = requests.get(url)
    print(f"Fetching data for {icao} from {url}")
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('tbody')
    print(f"Table found: {table is not None}")
    
    if table:
        rows = table.find_all('tr')

        print(f"Number of rows found: {len(rows)}")
        for row in rows:
            print(f"Row: {row}")

            cols = row.find_all('td')
            print(f"Columns: {[col.text.strip() for col in cols]}")

            if len(cols) >= 2:
                name = cols[0].text.strip()
                type = cols[1].text.strip()

                insert_data(icao, name, type)

# Create tables and scrape data for each ICAO code
for icao in icao_codes:
    create_table(icao)
    scrape_data(icao)

# Close the database connection
conn.close()

