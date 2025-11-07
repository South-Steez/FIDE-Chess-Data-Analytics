import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime

# Question 1.1
# Read the CSV file into a pandas DataFrame
file_path = "fide_historical.csv"
fide_data = pd.read_csv(file_path)

# Question 1.2
# Display the first few rows of the dataset to understand its structure
print(fide_data.head())

# Question 1.3
# Display the DataFrame in table format with a summary
print(fide_data)
print(fide_data.info())

# Convert the 'ranking_date' column to datetime format, handling errors
fide_data['date'] = pd.to_datetime(fide_data['ranking_date'], format='%d-%m-%y', errors='coerce')

# Display rows with NaT (parsing errors)
rows_with_errors = fide_data[fide_data['date'].isna()]
print("Rows with Parsing Errors:")
print(rows_with_errors)

# Drop rows with parsing errors or handle them based on your specific case
fide_data = fide_data.dropna(subset=['date'])

# Display the updated DataFrame with the new 'date' column
print("\nUpdated DataFrame:")
print(fide_data.head())


# Question 1.4
# a. Display only Magnus Carlsen's data in tabular format
magnus_data = fide_data[fide_data['name'] == 'Carlsen, Magnus']
print("Magnus Carlsen's Data:")
print(magnus_data)

# b. Display the record where Magnus Carlsen achieved his highest FIDE rating
max_rating_record = magnus_data.loc[magnus_data['rating'].idxmax()]
print("\nMagnus Carlsen's Record with Highest FIDE Rating:")
print(max_rating_record)

# c. Display Magnus Carlsen’s FIDE rating over the years using a lineplot
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='rating', data=magnus_data)
plt.title("Magnus Carlsen's Rating Progress")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.show()

# d. Display ratings in descending order from the date 2017-06-27
descending_ratings = fide_data[fide_data['date'] >= '2017-06-27'].sort_values(by=['date', 'rating'], ascending=[True, False])
print("\nRatings in Descending Order from 2017-06-27:")
print(descending_ratings)

# e. Display Wesley So’s FIDE rating over the years using a lineplot
wesley_data = fide_data[fide_data['name'] == 'So, Wesley']
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='rating', data=wesley_data)
plt.title("Wesley So's Rating Progress")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.show()

# f. Display Kramnik Vladimir’s FIDE rating over the years using a lineplot
kramnik_data = fide_data[fide_data['name'] == 'Kramnik, Vladimir']
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='rating', data=kramnik_data)
plt.title("Kramnik Vladimir's Rating Progress")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.show()

# g. Display all three chess players’ ratings in one lineplot
# Filter data for specific players
selected_players = ['Carlsen, Magnus', 'So, Wesley', 'Kramnik, Vladimir']
selected_data = fide_data[fide_data['name'].isin(selected_players)]

# Plot FIDE Ratings for the selected players
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='rating', hue='name', data=selected_data)
plt.title("FIDE Ratings of Magnus Carlsen, Wesley So, and Kramnik Vladimir Over the Years")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.legend()
plt.show()

# Question 1.5
# Filter data for Magnus Carlsen and Garry Kasparov
selected_players = ['Carlsen, Magnus', 'Kasparov, Garry']
selected_data = fide_data[fide_data['name'].isin(selected_players)]

# Plot FIDE Ratings for Magnus Carlsen and Garry Kasparov
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='rating', hue='name', data=selected_data)
plt.title("FIDE Ratings of Magnus Carlsen and Garry Kasparov Over the Years")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.legend()
plt.show()

 # Question 1.6
 # Filter data for Magnus Carlsen
carlsen_data = fide_data[fide_data['name'] == 'Carlsen, Magnus']

# Calculate the average or median rating for the rest of the world
world_data = fide_data[fide_data['name'] != 'Carlsen, Magnus']
world_average_rating = world_data.groupby('date')['rating'].mean()

# Plot FIDE Ratings for Magnus Carlsen and the rest of the world
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='rating', data=carlsen_data, label='Magnus Carlsen')
sns.lineplot(x=world_average_rating.index, y=world_average_rating.values, label='Rest of the World', color='orange')
plt.title("FIDE Ratings Comparison: Magnus Carlsen vs. Rest of the World")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.legend()
plt.show()

# Question 1.7
# Filter data for players after 2007-01-01 and not including Magnus Carlsen
filtered_players = fide_data[(fide_data['date'] > '2007-01-01') & (fide_data['name'] != 'Carlsen, Magnus')]

# Create an array of unique chess players meeting the criteria
unique_players_after_2007 = filtered_players['name'].unique()

# Display the array
print(unique_players_after_2007)

# Question 1.8
# Filter data for players after 2007-01-01 and not including Magnus Carlsen
filtered_players = fide_data[(fide_data['date'] > '2007-01-01') & (fide_data['name'] != 'Carlsen, Magnus')]

# Plot FIDE Ratings for all chess players meeting the criteria
plt.figure(figsize=(12, 8))
sns.lineplot(x='date', y='rating', hue='name', data=filtered_players, palette='tab20', linewidth=2)
plt.title("FIDE Ratings of Chess Players After 2007-01-01 (Excluding Magnus Carlsen)")
plt.xlabel("Date")
plt.ylabel("FIDE Rating")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
