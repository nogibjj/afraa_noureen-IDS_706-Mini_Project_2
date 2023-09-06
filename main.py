"""main module"""
import pandas as pd

def display_movies_stats():
    """
    Display basic info about movies dataset
    """
    df = pd.read_csv("MoviesTopRated")
    df.head()
    return df.shape