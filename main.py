"""main module"""
import pandas as pd

def display_highest_votes():
    """
    Display basic info about movies dataset
    """
    data_f = pd.read_csv("MoviesTopRated.csv")
    new_df = data_f.query('vote_average == vote_average.max()')
    return new_df
