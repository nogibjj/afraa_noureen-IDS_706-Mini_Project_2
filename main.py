"""main module"""
import pandas as pd
import matplotlib.pyplot as plt

def display_highest_votes():
    """
    Display basic info about movies dataset
    """
    movies_df = pd.read_csv("MoviesTopRated.csv")
    vote_df = movies_df.query("vote_average == vote_average.max()")
    print("Summary Statistics of the Top Rated Movies Dataset:\n")
    print(movies_df.describe())
    plt.figure(figsize=(10,6))
    plt.hist(movies_df["vote_average"], bins=10)
    plt.show()
    print("\nDetails of the movies that were given the highest votes are: \n")
    print(vote_df)
    return vote_df
