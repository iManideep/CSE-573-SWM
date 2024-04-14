import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Attempt to load the CSV file with a different encoding
try:
    linkedin_jobs_data = pd.read_csv(r'DATA\linkedin-jobs.csv', encoding='latin1')
except Exception as e:
    error_message = str(e)
    linkedin_jobs_data = None

if linkedin_jobs_data is not None:
    linkedin_jobs_data_head = linkedin_jobs_data.head()
    linkedin_jobs_data_columns = linkedin_jobs_data.columns.tolist()
    linkedin_jobs_data_head, linkedin_jobs_data_columns
else:
    error_message


# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Data processing for visualization
location_counts = linkedin_jobs_data['Location'].value_counts().head(10)
company_counts = linkedin_jobs_data['Company'].value_counts().head(10)
title_counts = linkedin_jobs_data['Title'].value_counts().head(10)

# Creating subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

# Plot for Distribution of Jobs by Location
sns.barplot(x=location_counts.values, y=location_counts.index, ax=axes[0], palette="viridis")
axes[0].set_title('Top 10 Job Locations')
axes[0].set_xlabel('Number of Jobs')
axes[0].set_ylabel('Location')

# Plot for Top Companies Posting Jobs
sns.barplot(x=company_counts.values, y=company_counts.index, ax=axes[1], palette="coolwarm")
axes[1].set_title('Top 10 Companies Posting Jobs')
axes[1].set_xlabel('Number of Jobs')
axes[1].set_ylabel('Company')

# Plot for Frequency of Job Titles
sns.barplot(x=title_counts.values, y=title_counts.index, ax=axes[2], palette="cubehelix")
axes[2].set_title('Top 10 Job Titles')
axes[2].set_xlabel('Number of Jobs')
axes[2].set_ylabel('Job Title')

# Adjust layout
plt.tight_layout()
plt.show()
