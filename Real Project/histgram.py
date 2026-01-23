import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Real Project/netflix_titles-2.csv')
print(df)

# Cleanning Data
df = df.dropna(subset=['type', 'title', 'director', 'cast', 'release_year', 'rating', 'country', 'duration', 'date_added',])


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