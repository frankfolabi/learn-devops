from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Joe Dee work?."""
    formatted_name = get_formatted_name('joe', 'dee')
    assert formatted_name == 'Joe Dee'

def test_first_last_middle():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
