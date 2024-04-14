import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the newly uploaded CSV file to check its content
file_path_laptop = r'DATA\Amazon.com _ laptop.csv'
amazon_laptop_data = pd.read_csv(file_path_laptop)

# Display the first few rows and the columns of the dataset
amazon_laptop_data_head = amazon_laptop_data.head()
amazon_laptop_data_columns = amazon_laptop_data.columns.tolist()

# Data processing for visualizations

# Clean the Price column to make it numerical
amazon_laptop_data['Cleaned Price'] = amazon_laptop_data['Price'].str.extract('(\d+,\d+|\d+)')[0].str.replace(',', '').astype(float)

# Calculate average ratings by brand
average_ratings_by_brand = amazon_laptop_data.groupby('Brand')['Rating'].mean().sort_values(ascending=False)

# Prepare data for RAM vs Price scatter plot
# Clean the RAM column to make it numerical for plotting
amazon_laptop_data['Cleaned RAM'] = amazon_laptop_data['RAM'].str.extract('(\d+)')[0].astype(int)

# Creating subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

# Plot for Distribution of Laptop Prices
sns.histplot(amazon_laptop_data['Cleaned Price'], bins=30, kde=True, ax=axes[0], color='blue')
axes[0].set_title('Distribution of Laptop Prices')
axes[0].set_xlabel('Price ($)')
axes[0].set_ylabel('Frequency')

# Plot for Average Ratings by Brand
average_ratings_by_brand.plot(kind='bar', ax=axes[1], color='green')
axes[1].set_title('Average Ratings by Brand')
axes[1].set_xlabel('Brand')
axes[1].set_ylabel('Average Rating')

# Plot for RAM vs. Price
sns.scatterplot(x='Cleaned RAM', y='Cleaned Price', data=amazon_laptop_data, ax=axes[2], color='red')
axes[2].set_title('RAM vs. Price')
axes[2].set_xlabel('RAM (GB)')
axes[2].set_ylabel('Price ($)')

# Adjust layout
plt.tight_layout()
plt.show()
