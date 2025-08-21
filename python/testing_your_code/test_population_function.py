from population_function import population

def test_population():
    """Test for the city function works on Ibadan, Nigeria - population 1000000."""
    result = population('ibadan', 'nigeria', 1_000_000)
    assert result == 'Ibadan, Nigeria - population 1000000'
