import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Real Project/netflix_titles-2.csv')
print(df)

# Cleanning Data
df = df.dropna(subset=['type', 'title', 'director', 'cast', 'release_year', 'rating', 'country', 'duration', 'date_added',])
