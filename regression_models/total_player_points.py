import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Given box score data
advanced_box_score = [
    [.610, .614, .227, .182, 9.9, 28.8, 20.0, 45.3, 1.4, 2.2, 7.8, 31.8, 133, 109, 15.0],
    [.776, .750, .250, .167, 3.3, 2.9, 3.1, 3.5, 4.2, 2.2, 18.9, 19.6, 122, 111, 1.9],
    [.682, .682, .182, .000, 6.9, 14.9, 11.2, 17.9, 2.9, 2.2, 0.0, 14.1, 155, 110, 8.6],
    [.756, .731, .385, .154, 0.0, 6.1, 3.3, 22.9, 0.0, 2.3, 6.7, 19.4, 150, 119, 5.0],
    [.462, .462, .692, .000, 8.0, 34.6, 22.2, 8.0, 3.3, 0.0, 0.0, 19.3, 111, 104, -0.2],
    [.500, .500, .625, .000, 0.0, 13.0, 7.0, 4.7, 2.1, 0.0, 20.0, 18.6, 82, 114, -8.2],
    [.425, .400, .200, .400, 6.2, 10.8, 8.7, 11.5, 0.0, 4.1, 14.5, 15.9, 97, 117, -6.2],
    [.515, .333, .333, .667, 0.0, 0.0, 0.0, 9.3, 0.0, 0.0, 20.5, 18.6, 96, 123, -12.0],
    [.500, .500, 1.000, .000, 0.0, 0.0, 0.0, 0.0, 0.0, 7.3, 25.0, 16.5, 71, 118, -9.4],
]

basic_box_score = [
    [36.11, 4, 12, .333, 2, 5, .400, 1, 2, .500, 0, 4, 4, 7, 1, 3, 3, 11, 1],
    [34.09, 6, 17, .353, 1, 2, .500, 4, 4, 1.000, 1, 7, 8, 4, 2, 2, 3, 17, -17],
    [31.20, 4, 11, .364, 1, 2, .500, 5, 7, .714, 4, 4, 8, 4, 0, 2, 2, 14, -14],
    [29.53, 6, 8, .750, 4, 6, .667, 2, 2, 1.000, 1, 2, 3, 1, 1, 1, 0, 18, -14],
    [29.00, 10, 16, .625, 1, 4, .250, 0, 1, .000, 1, 7, 8, 5, 0, 0, 1, 21, 7],
    [24.04, 3, 8, .375, 2, 5, .400, 0, 0, 0, 0, 3, 3, 1, 0, 2, 0, 8, 11],
    [19.20, 2, 5, .400, 0, 1, .000, 1, 2, .500, 1, 2, 3, 2, 1, 1, 1, 5, 5],
    [11.44, 1, 3, .333, 0, 1, .000, 2, 2, 1.000, 0, 0, 0, 1, 0, 1, 2, 4, -3],
    [10.50, 1, 3, .333, 1, 3, .333, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 1]
]

# Convert box score data to pandas DataFrame
advanced_df = pd.DataFrame(advanced_box_score, columns=["FG%", "3P%", "FT%", "TS%", "eFG%", "ORB%", "DRB%", "TRB%", "AST%", "STL%", "BLK%", "TOV%", "USG%", "ORTG", "Points"])
basic_df = pd.DataFrame(basic_box_score, columns=["MPG", "FGM", "FGA", "3PM", "3PA", "FTM", "FTA", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "Points"])

# Combine the two DataFrames
combined_df = pd.concat([advanced_df, basic_df], axis=1)

# Remove redundant "Points" column from advanced_df
advanced_df.drop(columns=["Points"], inplace=True)

# Split the data into features and target variable
X = combined_df.drop(columns=["Points"])  # Features
y = combined_df["Points"]  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)

# Hypothetical player's box score data (use relevant features)
hypothetical_player_data = [[30, 8, 0.500, 2, 4, 0.650, 0.625, 120]]  # adjust features

# Create a DataFrame for the hypothetical player
hypothetical_player_df = pd.DataFrame(hypothetical_player_data, columns=X.columns)

# Predict points for the hypothetical player
predicted_points = model.predict(hypothetical_player_df)

print("Predicted points for the hypothetical player:", predicted_points[0])
