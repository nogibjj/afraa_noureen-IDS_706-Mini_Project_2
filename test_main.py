"""test_main module"""
import main

def test_main():
    '''
    testing function for main
    '''
    new_vote_avg = main.display_movies_stats()
    assert new_vote_avg == 8.7
