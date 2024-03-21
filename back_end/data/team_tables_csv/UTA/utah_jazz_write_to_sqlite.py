from data.team_tables_csv.lite_sql_pandas import Lite_SQL


team = 'UTA'
team_name = 'utah_jazz'
database_ob = Lite_SQL(team_name)
database_ob.all_csv_tables_to_sqlite(team, team_name)





