import pandas as pd
import os


def update_dataframe(csv_file, dataframe_dict):
    # Extract game details from file name
    game_details = os.path.basename(csv_file).split('_')[3:-1]
    game_details = ' '.join(game_details)

    # Read the CSV file into a DataFrame
    new_data = pd.read_csv(csv_file)

    # Iterate over each row in the CSV file
    for index, row in new_data.iterrows():
        player_name = row['Starters']

        # Check if the player's data already exists in the dictionary
        if player_name in dataframe_dict:
            # If the player's data exists, append the row to the existing DataFrame
            row['GameDetails'] = game_details  # Add game details column
            dataframe_dict[player_name] = pd.concat([dataframe_dict[player_name], row.to_frame().T], ignore_index=True)
        else:
            # If the player's data doesn't exist, create a new DataFrame for that player
            player_df = pd.DataFrame(row).T
            player_df['GameDetails'] = game_details  # Add game details column
            dataframe_dict[player_name] = player_df

    return dataframe_dict


def sort_csv_tables_by_player(folder_path):
    dataframe_dict = {}
    # Iterate over each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            dataframe_dict = update_dataframe(file_path, dataframe_dict)

    # Save each player's DataFrame to separate CSV files
    for player_name, player_dataframe in dataframe_dict.items():
        player_dataframe.to_csv(f'{player_name}_data.csv', index=False)


if __name__ == "__main__":
    folder_path = './advanced_clean'
    sort_csv_tables_by_player(folder_path)
