import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd

# Load the newly uploaded CSV file to check its content
file_path_twitter = r'DATA\twitter.csv'
twitter_data = pd.read_csv(file_path_twitter)

# Display the first few rows and the columns of the dataset
twitter_data_head = twitter_data.head()
twitter_data_columns = twitter_data.columns.tolist()

# Data processing for visualizations

# Convert 'Joined' to datetime
twitter_data['Joined Date'] = pd.to_datetime(twitter_data['Joined'], errors='coerce')

# Plot for Timeline of Users Joining Twitter
twitter_data['Year Joined'] = twitter_data['Joined Date'].dt.year

twitter_data['Cleaned Followers'] = twitter_data['Followers'].str.replace('M', 'e6').str.replace('K', 'e3').astype(float)
twitter_data['Cleaned Following'] = twitter_data['Following'].str.replace('M', 'e6').str.replace('K', 'e3').str.replace(',', '').astype(float)

# Recompute the 'Year Joined' after correcting previous errors
twitter_data['Year Joined'] = twitter_data['Joined Date'].dt.year

# Convert 'Joined' to datetime properly
twitter_data['Joined Date'] = pd.to_datetime(twitter_data['Joined'], errors='coerce', format='%B %Y')
twitter_data['Year Joined'] = twitter_data['Joined Date'].dt.year

# Redo the visualizations with corrected data
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

# Plot for Distribution of Followers
sns.histplot(twitter_data['Cleaned Followers'], bins=30, ax=axes[0], color='purple')
axes[0].set_title('Distribution of Followers')
axes[0].set_xlabel('Followers')
axes[0].set_ylabel('Frequency')

# Plot for Timeline of Users Joining Twitter
twitter_data['Year Joined'].dropna().astype(int).value_counts().sort_index().plot(kind='bar', ax=axes[1], color='orange')
axes[1].set_title('Timeline of Users Joining Twitter')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Number of Users')

# Plot for Followers vs. Following
sns.scatterplot(x='Cleaned Following', y='Cleaned Followers', data=twitter_data, ax=axes[2], color='green')
axes[2].set_title('Followers vs. Following')
axes[2].set_xlabel('Following')
axes[2].set_ylabel('Followers')

# Adjust layout
plt.tight_layout()
plt.show()