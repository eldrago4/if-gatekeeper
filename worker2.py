import requests
from bs4 import BeautifulSoup

def scrape_gates(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the gate information
    tables = soup.find_all('table')
    gate_table = tables[1]  # The second table contains the gate information
    # Extract the headers
    headers = [header.text for header in gate_table.find_all('th')]
    # Extract the rows
    rows = []
    for row in gate_table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        row_data = [column.text.strip() for column in columns]
        rows.append(row_data)

    return headers, rows

def generate_sql_query(icao):
    return f"CREATE TABLE {icao} (NAME VARCHAR(30), TYPE VARCHAR(15), CLASS VARCHAR(2), MAX_AIRCRAFT_SIZE VARCHAR(30));"

def write_to_file(file_name, icao, headers, rows):
    with open(file_name, 'a') as f:
        f.write(generate_sql_query(icao) + '\n')
        for row in rows:
            f.write(f"INSERT INTO {icao} VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}');\n")

def main():
    icao_codes = [
        "KATL", "ZBAA", "OMDB", "RJTT", "KLAX", "ZSPD", "EHAM", "LFPG", "EDDF", "VHHH",
        "WSSS", "EGLL", "KORD", "RKSI", "YSSY", "LEMD", "MMMX", "SBGR", "VTBS", "LEBL",
        "FAOR", "ZGGG", "EGCC", "OMAA", "CYYZ", "WMKK", "ZGSZ", "UUEE", "OTHH", "LSZH",
        "EIDW", "VTSM", "LOWW", "LIRF", "NZAA", "LFPO", "EBBR", "EDDM", "LKPR", "LLBG",
        "NZWN", "EGSS", "EDDS", "ESSA", "LFLL", "EKCH", "LIRN", "EHGG", "LIMC"
    ]
    file_name = '50icao.txt'
    for icao in icao_codes:
        url = f'https://ifatc.org/gates?code={icao.lower()}'
        headers, rows = scrape_gates(url)
        write_to_file(file_name, icao, headers, rows)

if __name__ == '__main__':
    main()