# Step 01 Import all library
import pandas as pd
import matplotlib.pyplot as plt

#load the data
df = pd.read_csv('Real Project/netflix_titles-2.csv')
print(df)

# Cleanning Data
df = df.dropna(subset=['type', 'title', 'director', 'cast', 'release_year', 'rating', 'country', 'duration', 'date_added',])

type_counts = df['type'].value_counts()
plt.figure(figsize = (6, 4))

plt.bar(type_counts.index, type_counts.values, color = ['skyblue', 'orange'])
plt.title('Number of Movies VS TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()

plt.savefig('movies_vs_TVshows.png')
plt.show()

# Filter of Rating Data in PIE CHARTS
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_counts, labels=rating_counts.index, autopct = '%1.1f%%', startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('Content Ratings Of PIE Charts')
plt.show()

import matplotlib.pyplot as plt

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = (
    movie_df['duration']
    .str.replace('min', '', regex=False)
    .astype(int)
)

plt.figure(figsize=(8, 6))
plt.hist(
    movie_df['duration_int'],
    bins=30,
    color='purple',
    edgecolor='black'
)

plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')

plt.tight_layout()
plt.savefig('movie_duration_histogram.png', dpi=300, bbox_inches='tight')
plt.show()

#Scatter Plot

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.scatter(
    release_counts.index,     
    release_counts.values,
    color='red'
)
plt.title('Release Year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of counts')
plt.tight_layout()
plt.savefig('release_year_Scatter.png')
plt.show()

