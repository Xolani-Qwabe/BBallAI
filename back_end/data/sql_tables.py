from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import re
from teams_enum import NBATeam
from datetime import datetime


def send_request_for_one_html_page_to_site(url):
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'
        })
        response.raise_for_status()
        print("Thread going to sleep for 5 seconds request sent")
        time.sleep(5)
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def get_all_tables(page):
    tables = page.find_all('table')
    return tables

def html_table_to_sqlite(html_table):
    rows = html_table.find_all('tr')
    conn = sqlite3.connect('new_stats.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS GSW_basicH2 
                    (Player TEXT, MP TEXT, FG INTEGER, FGA INTEGER, FG_PCT TEXT, 
                    FG3 INTEGER, FG3A INTEGER, FG3_PCT TEXT, FT INTEGER, FTA INTEGER, 
                    FT_PCT TEXT, ORB INTEGER, DRB INTEGER, TRB INTEGER, AST INTEGER, 
                    STL INTEGER, BLK INTEGER, TOV INTEGER, PF INTEGER, PTS INTEGER, 
                    PLUS_MINUS TEXT)''')
    for row in rows[2:]:
        print(len(row))
        print(row)
        cols = row.find_all(['th', 'td'])
        values = [col.get_text() for col in cols]
        if len(values) == 21:  # ensure we have all columns filled
            cursor.execute('INSERT INTO GSW_basicH2  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def get_game_details_joined_for_table(page):
    details = page.find(id='content').find('h1').get_text()
    return details.replace(' ', '').replace(',', '_')


def get_game_info(game_string):
    # Regular expression pattern to extract game details, team names, and date
    pattern = r'(?:In-SeasonTournamentFinal:)?([A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)*)at([A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)*)BoxScore_(\w+\d+_\d+)'
    # Extracting information from each string
    match = re.match(pattern, game_string)
    if match:
        team1 = match.group(1)
        team2 = match.group(2)
        date = match.group(3)
        # Insert spaces between camel case team names
        away = re.sub(r"(?<=\w)([A-Z])", r" \1", team1)
        home = re.sub(r"(?<=\w)([A-Z])", r" \1", team2)
        date_obj = datetime.strptime(date, '%B%d_%Y')
        nba = NBATeam
        formatted_date = date_obj.strftime('%Y-%m-%d')
        print("Game:", away, "@", home)
        return (nba.get_team_abbreviation(away), nba.get_team_abbreviation(home),
                formatted_date, f"{away} @ {home}")
    else:
        print("No match found for:", game_string)


tables = get_all_tables(send_request_for_one_html_page_to_site('https://www.basketball-reference.com/boxscores/202402010BOS.html'))
# print((tables[8]))
# # write_html_tables_to_sqlite(tables[10])
html_table_to_sqlite(tables[14])

