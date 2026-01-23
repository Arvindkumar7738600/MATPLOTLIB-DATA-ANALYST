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



country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index,
          country_counts.values,
          color = 'teal'
)
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number')
plt.ylabel('Country')
plt.tight_layout()

plt.savefig('Top 10 Countries.png')
plt.show()


content_by_year = df.groupby(['release_year', 'type']) .size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))
#first subplot:movies
ax [0]. plot (content_by_year.index, content_by_year ['Movie'], color= 'blue')
ax [0]. set_title('Movies Released Per Year')
ax [0]. set_xlabel('Year')
ax [0]. set_ylabel( 'Number of Movies')


#second subplot: TV Shows
ax [0]. plot (content_by_year.index, content_by_year ['TV Show'], color='orange')
ax [0]. set_title('TV Shows Released Per Year')
ax [0]. set_xlabel( 'Year')
ax [0]. set_ylabel ( 'Number of Movies')


fig.suptitle('Compare of Movie and TV showa Released Over Years')

plt.tight_layout()
plt.savefig('movies and tv shows Released Data')
plt.show()