"""main module"""
import pandas as pd


def display_highest_votes():
    """
    Display basic info about movies dataset
    """
    movies_df = pd.read_csv("MoviesTopRated.csv")
    vote_df = movies_df.query("vote_average == vote_average.max()")
    print(movies_df.describe())
    print("\nDetails of the movies that were given the highest votes are: \n")
    print(vote_df)
    return vote_df
