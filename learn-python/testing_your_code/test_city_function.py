from city_function import city

def test_city():
    """Test for the city function works on Ibadan, Nigeria."""
    result = city('ibadan', 'nigeria')
    assert result == 'Ibadan, Nigeria'
