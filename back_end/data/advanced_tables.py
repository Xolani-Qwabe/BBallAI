import sqlite3
from bs4 import BeautifulSoup
import requests
import time
import datetime as dt
from datetime import datetime
import re
from teams_enum import NBATeam




advanced_schema = '''CREATE TABLE IF NOT EXISTS advanced_boxscore_stats (
player_name TEXT,
 minutes TEXT,
  true_shooting_pct TEXT,
   effective_FG_pct TEXT,
     _3P_attempts_rate TEXT,
      FT_rate TEXT,
       ORB_pct TEXT,
        DRB_pct TEXT,
         TRB_pct TEXT,
          AST_pct TEXT,
           STL_pct TEXT,
            BLK_pct TEXT,
             TOV_pct TEXT,
              USG_pct TEXT,
               ORtg TEXT,
                DRtg TEXT,
                 BPM TEXT)'''


def extract_table_id_info_from_table(table_html):
    table_id = table_html['id']
    parts = table_id.split("-")
    team_abbr = parts[1]
    time_frame = parts[2]
    table_type_ = parts[3]
    return team_abbr, time_frame, table_type_


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


def get_html_table_data(html_table):
    data = []
    for row in html_table.find_all('tr'):
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    print(data)
    return data


def create_database_table(conn,schema):
    c = conn.cursor()
    c.execute(schema)


def insert_data_into_table(conn, data):
    c = conn.cursor()
    for row in data:
        if len(row) == 17:
            c.execute('INSERT INTO advanced_stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
        if len(row) == 21:  # ensure we have all columns filled
            c.execute('INSERT INTO basic_stats  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
    conn.commit()


def write_table_to_sqlite(table, database, schema_to_create):
    data = get_html_table_data(table)
    conn = sqlite3.connect(database)
    create_database_table(conn, schema_to_create)
    insert_data_into_table(conn, data)
    conn.close()
    print("Table written to SQLite database successfully.")


def time_string_to_timedelta(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return dt.timedelta(minutes=minutes, seconds=seconds)



page = send_request_for_one_html_page_to_site('https://www.basketball-reference.com/boxscores/202310240GSW.html')
tables = get_all_tables(page)
# print(tables[0])


team_id, timeframe, table_type = extract_table_id_info_from_table(tables[7])
print("team_id:", team_id)
print("time_frame:", timeframe)
print("table_type:", table_type)

game_detatils = get_game_details_joined_for_table(page)
away, home, date, game_info = get_game_info(game_detatils)
print("away:", away)
print("home:", home)
print("date:", date)
print("game_info:", game_info)
print("game_id", home+away+date)

# write_table_to_sqlite(tables[7])
# write_table_to_sqlite(tables[15])