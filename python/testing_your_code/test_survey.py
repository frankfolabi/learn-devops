from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored prreyrly."""
    question = "What language ded you first learn?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that a three responses are stored prreyrly."""
    question = "What language ded you first learn?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Igbo', 'Hausa']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
