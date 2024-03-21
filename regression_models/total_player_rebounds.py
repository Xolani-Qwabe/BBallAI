from sklearn.linear_model import LinearRegression
import numpy as np

# Aggregate player statistics from over 55 games
player_minutes = np.array([30, 25, 28, 32, 29, ...])  # Stats for all 55+ games
off_reb_percent = np.array([0.15, 0.12, 0.14, 0.16, 0.13, ...])
def_reb_percent = np.array([0.20, 0.18, 0.19, 0.22, 0.17, ...])
total_reb_percent = np.array([0.35, 0.30, 0.33, 0.38, 0.30, ...])
def_rating = np.array([105, 100, 110, 98, 105, ...])
player_height = np.array([6.6, 6.7, 6.5, 6.8, 6.6, ...])
player_wingspan = np.array([6.9, 6.8, 6.7, 6.9, 6.8, ...])

# Aggregate opponent statistics from over 55 games
opp_height = np.array([6.8, 6.7, 6.9, 6.6, 6.8, ...])
opp_wingspan = np.array([7.1, 7.0, 7.2, 6.9, 7.1, ...])
opp_off_reb_percent = np.array([0.14, 0.16, 0.15, 0.13, 0.12, ...])
opp_def_reb_percent = np.array([0.21, 0.20, 0.23, 0.19, 0.18, ...])

# Aggregate team statistics from over 55 games
team_rebounds = np.array([45, 40, 42, 48, 38, ...])
opp_team_rebounds = np.array([48, 50, 46, 52, 45, ...])

X = np.column_stack((player_minutes, off_reb_percent, def_reb_percent, total_reb_percent, def_rating,
                     team_rebounds, opp_team_rebounds, player_height, player_wingspan,
                     opp_height, opp_wingspan, opp_off_reb_percent, opp_def_reb_percent))

# Assuming y contains the total rebounds for each game in the same order as the X data
y = np.array([...])  # Total rebounds for all 55+ games

model = LinearRegression()
model.fit(X, y)

# Predict total rebounds for the next game using data from the 56th game
next_game_data = np.array([...])  # Data for the 56th game

predicted_total_rebounds = model.predict(next_game_data.reshape(1, -1))

print("Predicted total rebounds in the next game based on 55+ games data:", predicted_total_rebounds[0])
