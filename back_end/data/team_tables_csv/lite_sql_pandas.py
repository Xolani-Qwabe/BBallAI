import pandas as pd
import sqlite3
import os


class Lite_SQL:
    def __init__(self, name="SQL_Object"):
        self.name = name

    @staticmethod
    def write_csv_to_sqlite(csv_file_path, table_name, db_file_path):
        table = pd.read_csv(csv_file_path)
        print(table)
        conn = Lite_SQL.create_or_connect_to_db(db_file_path)
        table.to_sql(table_name, conn, if_exists='replace', index=False)
        # conn.close()

    @staticmethod
    def read_table_sqlite(table_name, db_file_path):
        conn = sqlite3.connect(db_file_path)
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, conn)
        print(df)

    @staticmethod
    def create_or_connect_to_db(db_name):
        if not os.path.exists(db_name):
            print(f"Database '{db_name}' does not exist. Creating it...")
            conn = sqlite3.connect(db_name)
            # conn.close()

            print(f"Database '{db_name}' created successfully.")
        else:
            print(f"Database '{db_name}' already exists. Connecting to it...")
            conn = sqlite3.connect(db_name)
        return conn

    def __repr__(self):
        pass


    def all_csv_tables_to_sqlite(self, team_name, team_table_name):
    #paths to csv tables
        roster_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Roster.csv"
        advanced_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Advanced.csv"
        pbp_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Pbp.csv"
        per_game_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Per_game.csv"
        per_minute_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Per_minute.csv"
        per_pos_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Per_poss.csv"
        adjusted_shooting_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Adj_shooting.csv"
        salaries_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Salaries2.csv"
        shooting_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Shooting.csv"
        team_info_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Team_misc.csv"
        team_and_opponent_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Team_and_opponent.csv"
        totals_file_path = fr"C:\Users\thabi\Desktop\test_sel_tut\data\team_tables_csv\{team_name}\{team_name}_Totals.csv"
    #write csv files to sqlite
        self.write_csv_to_sqlite(advanced_file_path, f'{team_name}_advanced', f'{team_table_name}_advanced.db')
        self.write_csv_to_sqlite(roster_file_path, f'{team_name}_roster', f'{team_table_name}_roster.db')
        self.write_csv_to_sqlite(pbp_file_path, f'{team_name}_pbp', f'{team_table_name}_pbp.db')
        self.write_csv_to_sqlite(per_game_file_path, f'{team_name}_per_game', f'{team_table_name}_per_game.db')
        self.write_csv_to_sqlite(per_minute_file_path, f'{team_name}_per_minute', f'{team_table_name}_per_minute.db')
        self.write_csv_to_sqlite(per_pos_file_path, f'{team_name}_per_possession',f'{team_table_name}_per_possession.db')
        self.write_csv_to_sqlite(adjusted_shooting_file_path, f'{team_name}_adjusted_shooting',f'{team_table_name}_adjusted_shooting.db')
        self.write_csv_to_sqlite(salaries_file_path, f'{team_name}_salaries', f'{team_table_name}_salaries.db')
        self.write_csv_to_sqlite(shooting_file_path, f'{team_name}_shooting', f'{team_table_name}_shooting.db')
        self.write_csv_to_sqlite(team_info_file_path, f'{team_name}_team_info', f'{team_table_name}_team_info.db')
        self.write_csv_to_sqlite(team_and_opponent_file_path, f'{team_name}_team_and_opponent',f'{team_table_name}_team_and_opponent.db')
        self.write_csv_to_sqlite(totals_file_path, f'{team_name}_totals', f'{team_table_name}_totals.db')
