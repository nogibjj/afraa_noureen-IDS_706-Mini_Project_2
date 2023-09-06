"""main module"""
import pandas as pd

def display_movies_stats():
    """
    Display basic info about movies dataset
    """
    df = pd.read_csv("MoviesTopRated.csv")
    return df.loc["0","vote_average"]
