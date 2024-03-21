import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

player_minutes = [30, 25, 28, 32, 29, 27, 26]
usage_rate = [0.25, 0.28, 0.3, 0.27, 0.29, 0.26, 0.28]
avg_shots_attempted = [20 ,21 ,24 ,23 ,17 ,19 ,15]
fg_percentage = [0.45 ,0.48 ,0.42 ,0.47 ,0.46 ,0.40 ,0.41]
opp_defensive_rating = [105 ,100 ,110 ,98 ,105 ,95 ,97]
total_points = [24 ,20 ,22 ,26 ,25 ,21 ,23]

# Determine if opponent's defensive rating is higher than average
avg_defensive_rating = np.mean(opp_defensive_rating)
opponent_higher_defensive_rating = [1 if rating > avg_defensive_rating else 0 for rating in opp_defensive_rating]

# Reshape data for regression
X = np.array([player_minutes,
              usage_rate,
              avg_shots_attempted,
              fg_percentage,
              opp_defensive_rating,
              total_points,
              opponent_higher_defensive_rating]).T

y = np.array(avg_shots_attempted)

# Normalize the input data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Create and fit the model
model = LinearRegression()
model.fit(X_normalized,y)

# Predict shots attempted for the next game with lower FG percentage
next_game_minutes = 27
next_game_usage_rate = 0.28
next_game_fg_percentage = 0.35  # Lower FG percentage for prediction
next_game_opp_defensive_rating = 110
next_game_total_points = 23
next_game_opponent_higher_defensive_rating = int(next_game_opp_defensive_rating > avg_defensive_rating)

# Normalize the prediction data
X_predict = scaler.transform([[next_game_minutes,
                               next_game_usage_rate,
                               np.mean(avg_shots_attempted),
                               next_game_fg_percentage,
                               next_game_opp_defensive_rating,
                               next_game_total_points,
                               next_game_opponent_higher_defensive_rating]])

predicted_shots_attempted = model.predict(X_predict)

print("Predicted shots attempted in the next game with a lower field goal percentage:", predicted_shots_attempted[0])