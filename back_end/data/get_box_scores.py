import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re as r
from datetime import datetime
from teams_enum import NBATeam


"""
Function takes a url and returns a html page 
served by site using bs4
"""


def send_request_for_one_html_page_to_site(url):
    """Handles HTTP Status Code errors"""
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'
        })
        response.raise_for_status()  # Raises an HTTPError for bad responses
        print("Thread going to sleep for 5 seconds request sent")
        time.sleep(5)
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def get_multiple_html_pages_from_site(links):
    pages = []
    for link in links:
        response = requests.get(link, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'
        },)
        time.sleep(3)
        pages.append(BeautifulSoup(response.content, 'html.parser'))
    return pages


def get_tables(page):
    tables = page.find_all('table')
    return tables


def get_all_tables(page):
    tables = page.find_all('table')
    return tables


"""
finds the header with #id content and 
grabs the inner text which is the game details on site
"""


def get_game_details_as_is(page):
    return page.find(id='content').find('h1').get_text()


def get_game_details_joined_for_table(page):
    details = page.find(id='content').find('h1').get_text()
    return details.replace(' ', '').replace(',', '_')


def get_basic_table_headers(table):
    return [th.getText().split('\n') for th in table.find_all('tr', limit=5)[1:2]][0][1:-1]


def get_advanced_table_headers(table):
    headers = [th.getText().split('\n') for th in table.find_all('tr')[1]]
    clean = [header for header in headers if header != ['', '']]
    return [item for new_array in clean for item in new_array]


def get_table_rows(table):
    return [td for td in table.find('tbody').find_all('tr')]


def get_table_data(rows):
    player_stats = [[td.getText() for td in rows[i].find_all('td')] for i in range(len(rows))]
    player_names = [[td.getText() for td in rows[i].find_all('a')] for i in range(len(rows))]
    return player_names, player_stats


def make_table_rows(player_names, player_stats):
    """Check if there is a string time object in player stats
    and change function to return a list with made rows with player names"""
    player_names[5].insert(5, 'player')
    for i in range(len(player_names)):
        player = player_names[i][0]
        (player_stats[i].insert(0, player))


def make_basic_table_pandas(basic_table,page):
    """Refactor"""
    rows = get_table_rows(basic_table)
    player_names, player_stats = get_table_data(rows)
    get_game_details = get_game_details_joined_for_table(page)
    away, home, date = get_game_info_list(get_game_details)
    [player_stat.append(away) for player_stat in player_stats]
    [player_stat.append(home) for player_stat in player_stats]
    [player_stat.append(date) for player_stat in player_stats]
    headers = get_advanced_table_headers(basic_table)
    headers.append("Away")
    headers.append("Home")
    headers.append("Date")
    make_table_rows(player_names, player_stats)
    df = pd.DataFrame(player_stats, columns=headers)
    df.fillna(0.0, inplace=True)
    df.replace('Did Not Play', '0:0', inplace=True)
    df.drop(5, inplace=True)
    return df


def make_advanced_table_pandas(adv_table,page):
    rows = get_table_rows(adv_table)
    player_names, player_stats = get_table_data(rows)
    get_game_details = get_game_details_joined_for_table(page)
    away, home, date = get_game_info_list(get_game_details)
    [player_stat.append(away) for player_stat in player_stats]
    [player_stat.append(home) for player_stat in player_stats]
    [player_stat.append(date) for player_stat in player_stats]
    headers = get_advanced_table_headers(adv_table)
    headers.append("Away",)
    headers.append("Home")
    headers.append("Date")
    make_table_rows(player_names, player_stats)
    df = pd.DataFrame(player_stats, columns=headers)
    df.fillna(0.0, inplace=True)
    df.replace('Did Not Play', '0:0', inplace=True)
    df.drop(5, inplace=True)
    return df


def write_basic_tables_to_file(details, basic_table_home, basic_table_away):
    path = '../reading_cleaning_data/box_score_tables_csv'
    home_path = f'{path}/basic_table_H_{details}.csv'
    away_path = f'{path}/basic_table_A_{details}.csv'
    pd.DataFrame.to_csv(basic_table_home, home_path)
    pd.DataFrame.to_csv(basic_table_away, away_path)


def write_advanced_tables_to_file(details, adv_table_home, adv_table_away):
    path = '../reading_cleaning_data/box_score_tables_csv'
    home_path = f'{path}/advanced_table_H_{details}.csv'
    away_path = f'{path}/advanced_table_A_{details}.csv'
    pd.DataFrame.to_csv(adv_table_home, home_path)
    pd.DataFrame.to_csv(adv_table_away, away_path)


def tables_to_csv(page):
    print('building basic tables with pandas')
    basic_table_home = make_basic_table_pandas(get_tables(page)[0],page)
    basic_table_away = make_basic_table_pandas(get_tables(page)[2],page)
    print('building advanced tables with pandas')
    adv_table_away = make_advanced_table_pandas(get_tables(page)[1],page)
    adv_table_home = make_advanced_table_pandas(get_tables(page)[3],page)
    game_details = get_game_details_joined_for_table(page)
    print(f'Writing tables for game {game_details} to.csv')
    write_basic_tables_to_file(game_details, basic_table_home, basic_table_away)
    write_advanced_tables_to_file(game_details, adv_table_home, adv_table_away)


def get_all_box_score_pages(links):
    pages = map(get_multiple_html_pages_from_site,links)
    print('Fetched all pages from basketball reference pages')
    return pages


def write_all_box_score_pages_to_csv():
    print('Getting HTML pages *********************************************')
    # links = list(get_all_box_score_links.all_box_score_links_2024_games())
    links = [ 'https://www.basketball-reference.com/boxscores/202402030CHI.html']
    print(len(links))
    pages = [send_request_for_one_html_page_to_site(url) for url in links]
    [tables_to_csv(page) for page in pages]


def get_game_info_list(game_string):
    # Regular expression pattern to extract game details, team names, and date
    pattern = r'(?:In-SeasonTournamentFinal:)?([A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)*)at([A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)*)BoxScore_(\w+\d+_\d+)'
    # Extracting information from each string
    match = r.match(pattern, game_string)
    if match:
        team1 = match.group(1)
        team2 = match.group(2)
        date = match.group(3)
        # Insert spaces between camel case team names
        team1 = r.sub(r"(?<=\w)([A-Z])", r" \1", team1)
        team2 = r.sub(r"(?<=\w)([A-Z])", r" \1", team2)
        date_obj = datetime.strptime(date, '%B%d_%Y')
        nba = NBATeam
        formatted_date = date_obj.strftime('%Y-%m-%d')
        print("Game:", team1, "at", team2)
        print("Date:", formatted_date)
        return [nba.get_team_abbreviation(team1), nba.get_team_abbreviation(team2), formatted_date]
    else:
        print("No match found for:", game_string)


if __name__ == '__main__':

 print(get_game_info_list( get_game_details_joined_for_table(send_request_for_one_html_page_to_site('https://www.basketball-reference.com/boxscores/202311010TOR.html'))))


