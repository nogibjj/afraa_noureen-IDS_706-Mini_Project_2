"""test_main module"""
import main

def test_main():
    '''
    testing function for main
    '''
    new_shape = main.display_movies_stats()
    assert new_shape != 0
