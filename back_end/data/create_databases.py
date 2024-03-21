import sqlite3


nba_teams_abbreviated = [
    "ATL", "BOS", "BRK", "CHI", "CLE", "DAL", "DEN", "DET", "GSW",
    "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK",
    "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS","CHO"
]

advanced_boxscore_schema = '''CREATE TABLE IF NOT EXISTS advanced_boxscore_stats (
player_name TEXT, minutes TEXT, true_shooting_pct TEXT, effective_fg_pct TEXT, 
_3p_attempts_rate TEXT, ft_rate TEXT, offensive_rebound_pct TEXT,defensive_rebound_pct TEXT,
total_rebound_pct TEXT,assist_pct TEXT, steal_pct TEXT, block_pct TEXT, turnover_pct TEXT,
usage_pct TEXT, offensive_rating TEXT, defensive_rating TEXT, box_plus_minus TEXT,Tteam_id TEXT,
time_frame TEXT, table_type TEXT, away_team_id TEXT, home_team_id TEXT,game_date TEXT,
game_info TEXT, game_id TEXT)'''

basic_boxscore_schema = '''CREATE TABLE IF NOT EXISTS basic_boxscore_stats 
(player_name TEXT, minutes TEXT, field_goal TEXT, field_goal_attempts TEXT,
 field_goal_pct TEXT, _3pt TEXT, _3pt_attempts TEXT, _3pt_pct TEXT,
ft TEXT,ft_attempts TEXT,ft_pct TEXT, offensive_rebound TEXT,
defensive_rebound TEXT, total_rebound TEXT, assists TEXT,steals TEXT,
blocks TEXT, turnovers TEXT, personal_fouls TEXT, points TEXT,plus_minus TEXT,
team_id TEXT,time_frame TEXT, table_type TEXT, away_team_id TEXT, home_team_id TEXT,
game_date TEXT,game_info TEXT, game_id TEXT)'''

roster_schema = '''CREATE TABLE IF NOT EXISTS roster (
                    jersey_id TEXT PRIMARY KEY,
                    player_name TEXT,
                    position TEXT,
                    height TEXT,
                    weight TEXT,
                    birth_date TEXT,
                    nationality TEXT,
                    years_pro TEXT,
                    college TEXT
                )'''

team_and_opponent_schema = '''CREATE TABLE IF NOT EXISTS team_and_opponent 
(name TEXT,games_played TEXT, minutes TEXT, field_goal TEXT, field_goal_attempts TEXT,
 field_goal_pct TEXT, _3pt TEXT, _3pt_attempts TEXT, _3pt_pct TEXT,_2pt TEXT,
_2pt_attempts TEXT, _2pt_pct TEXT, ft TEXT,ft_attempts TEXT,ft_pct TEXT, offensive_rebound TEXT,
defensive_rebound TEXT, total_rebound TEXT, assists TEXT,steals TEXT,
blocks TEXT, turnovers TEXT, personal_fouls TEXT, points TEXT)'''

team_misc_schema = '''CREATE TABLE IF NOT EXISTS team_info (
name_ TEXT,wins TEXT,losses TEXT, expected_wins TEXT, expected_losses TEXT,
margin_of_victory TEXT, strength_of_schedule TEXT, simple_rating_sys TEXT,
offeensive_rating TEXT, defensive_rating TEXT,pace TEXT, ft_attempt_rate TEXT,
_3pt_attempt_rate TEXT, effective_fg_pct TEXT, turnover_pct TEXT,
offensive_rebound_pct TEXT, ft_per_fg_attempt TEXT, opponent_effective_fg_pct TEXT,
opponent_turnover_pct TEXT,defensive_rebound_pct TEXT, opponent_ft_pct_per_fg_attempt TEXT,
 arena TEXT, attendance TEXT)'''


per_game_schema = '''CREATE TABLE IF NOT EXISTS per_game 
(rank TEXT,player_name TEXT,age TEXT,games TEXT,games_started TEXT,
 minutes TEXT, field_goal TEXT, field_goal_attempts TEXT,
 field_goal_pct TEXT, _3pt TEXT, _3pt_attempts TEXT, _3pt_pct TEXT,
 _2pt TEXT, _2pt_attempts TEXT,_2pt_pct TEXT,effective_fg_pct TEXT,
ft TEXT,ft_attempts TEXT,ft_pct TEXT, offensive_rebound TEXT,
defensive_rebound TEXT, total_rebound TEXT, assists TEXT,steals TEXT,
blocks TEXT, turnovers TEXT, personal_fouls TEXT, points TEXT)'''


totals_schema = '''CREATE TABLE IF NOT EXISTS totals 
(rank TEXT,player_name TEXT,age TEXT,games TEXT,games_started TEXT,
 minutes TEXT, field_goal TEXT, field_goal_attempts TEXT,
 field_goal_pct TEXT, _3pt TEXT, _3pt_attempts TEXT, _3pt_pct TEXT,
 _2pt TEXT, _2pt_attempts TEXT,_2pt_pct TEXT,effective_fg_pct TEXT,
ft TEXT,ft_attempts TEXT,ft_pct TEXT, offensive_rebound TEXT,
defensive_rebound TEXT, total_rebound TEXT, assists TEXT,steals TEXT,
blocks TEXT, turnovers TEXT, personal_fouls TEXT, points TEXT)'''

per_minute_schema = '''CREATE TABLE IF NOT EXISTS per_36 
(rank TEXT,player_name TEXT,age TEXT,games TEXT,games_started TEXT,
 minutes TEXT, field_goal TEXT, field_goal_attempts TEXT,
 field_goal_pct TEXT, _3pt TEXT, _3pt_attempts TEXT, _3pt_pct TEXT,
 _2pt TEXT, _2pt_attempts TEXT,_2pt_pct TEXT,
ft TEXT,ft_attempts TEXT,ft_pct TEXT, offensive_rebound TEXT,
defensive_rebound TEXT, total_rebound TEXT, assists TEXT,steals TEXT,
blocks TEXT, turnovers TEXT, personal_fouls TEXT, points TEXT)'''


per_100_possesion_schema = '''CREATE TABLE IF NOT EXISTS per_100_possesion 
(rank TEXT,player_name TEXT,age TEXT,games TEXT,games_started TEXT,
 minutes TEXT, field_goal TEXT, field_goal_attempts TEXT,
 field_goal_pct TEXT, _3pt TEXT, _3pt_attempts TEXT, _3pt_pct TEXT,
 _2pt TEXT, _2pt_attempts TEXT,_2pt_pct TEXT,
ft TEXT,ft_attempts TEXT,ft_pct TEXT, offensive_rebound TEXT,
defensive_rebound TEXT, total_rebound TEXT, assists TEXT,steals TEXT,
blocks TEXT, turnovers TEXT, personal_fouls TEXT, points TEXT,"" TEXT,
offensive_rating TEXT, defensive_rating TEXT)'''


advanced_schema = '''CREATE TABLE IF NOT EXISTS advanced (
rank TEXT, player_name TEXT, age TEXT,games TEXT, minutes TEXT, player_efficiency_rating TEXT,
 true_shooting_pct TEXT, _3p_attempt_rate TEXT, ft_attempt_rate TEXT, offensive_rebound_pct TEXT,
 defensive_rebound_pct TEXT,total_rebound_pct TEXT,assist_pct TEXT, steal_pct TEXT, block_pct TEXT,
turnover_pct TEXT,usage_pct TEXT,'' TEXT, offensive_win_shares TEXT, defensive_win_shares TEXT,
win_shares TEXT,win_shares_per_48 TEXT,' ' TEXT,offensive_box_plus_minus TEXT,defensive_box_plus_minus TEXT,
box_plus_minus TEXT,value_over_replacement_player TEXT)'''

adjusted_shooting_schema = '''CREATE TABLE IF NOT EXISTS adjusted_shooting 
(rank TEXT,player_name TEXT,age TEXT,games TEXT, minutes TEXT,'' TEXT,
 field_goal TEXT, _2pt TEXT, _3pt TEXT, effective_field_goal TEXT, 
ft TEXT, true_shooting TEXT,ft_rate TEXT,
_3pt_attempt_rate TEXT,' ' TEXT, fg_adjusted TEXT, 
_2p_adjusted TEXT,_3p_adjusted TEXT,effective_field_goal_adjusted TEXT,
 ft_adjusted TEXT, true_shooting_adjusted TEXT, ft_rate_adjusted TEXT,
  _3p_attempt_adjusted TEXT,'  ' TEXT, fg_added TEXT, true_shooting_added TEXT)'''


shooting_schema = '''CREATE TABLE IF NOT EXISTS shooting 
(rank TEXT,player_name TEXT,age TEXT,games TEXT, minutes TEXT,
 field_goal_pec TEXT,average_distance TEXT,pec_of_fga_by_distanceTEXT,
_2pt_range TEXT, _0_to_3_feet_attempt TEXT, _3_to_10_feet_attempt TEXT,
 _10_to_16_feet_attempt TEXT, _16_to_3pt_line_attempt TEXT, _3pt_line_attempt TEXT,
fg_by_distance TEXT,_2pt_fg TEXT,_0_to_3_feet_fg TEXT,_3_to_10_feet_fg TEXT, 
_10_to_16_feet_fg TEXT, _16_to_3pt_line_fg TEXT, _3pt_line_fg TEXT,
 pec_of_assisted_fg TEXT, _2p_assisted_fg TEXT, _3p_assisted_fg TEXT,dunks TEXT,
dunks_fg_attempt_pec TEXT,dunk_fg TEXT, corner_3pt TEXT, corner_3pt_attempt_pec TEXT,
corner_3pt_pec TEXT, heaves TEXT, heaves_attempt TEXT, heaves_fg TEXT)'''


play_by_play_schema = '''CREATE TABLE IF NOT EXISTS play_by_play 
(rank TEXT,player_name TEXT,age TEXT,games TEXT, minutes TEXT,
at_point_gaurd_pec TEXT, at_shooting_gaurd_pec TEXT, at_small_forward_pec TEXT,
at_power_forward_pec TEXT, at_center_pec TEXT, plus_minus_per_100_on_court TEXT,
plus_minus_per_100_off_court TEXT, turnover_bad_pass TEXT, turnover_lost_ball TEXT,
shooting_fouls TEXT, offensive_fouls TEXT,shooting_fouls_drawn TEXT, offensive_fouls_drawn TEXT,
points_generated_by_assist TEXT, and_1_fg TEXT, blocked_fg TEXT)'''


def create_database_and_schemas(team_name):
    schemas = [roster_schema,team_and_opponent_schema,
team_misc_schema,per_game_schema,per_minute_schema,per_100_possesion_schema,adjusted_shooting_schema,
shooting_schema,play_by_play_schema,advanced_schema,basic_boxscore_schema,advanced_boxscore_schema]

    db_name = f"nba_databases/{team_name}.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
    [cursor.execute(schema) for schema in schemas]
    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"SQLite database '{db_name}' created successfully.")


[create_database_and_schemas(team_name) for team_name in nba_teams_abbreviated]