import pytest
from project import get_required_hours, check_missing_hours, draft_email

def test_get_required_hours():
    #test that correct hours are extracted
    assert get_required_hours(11, 2025) == 145
    assert get_required_hours(12, 2025) == 130
    # Test what happens if no month is found
    # Your function calls sys.exit, so we check that SystemExit is raised
    with pytest.raises(SystemExit):
        get_required_hours(10, 2024)


def test_check_missing_hours():
    # Test with required hours = 150. 4 people on that list
    reminder_list = check_missing_hours(11,2025,150)
    assert len(reminder_list) == 4
    assert reminder_list[0]["name"] == "Daniel Ng"
    assert reminder_list[0]["hour input"] == "130"

    # Test with required hours = 100. No one should be on the list.
    reminder_list_low = check_missing_hours(11, 2025, 100)
    assert len(reminder_list_low) == 0


def test_draft_email():

    person = {"name": "David Test", "email": "test1@gmail.com", "hour input": "100"}
    subject, body = draft_email(person, 11, 2025, 160)

    # Test the subject
    assert subject == "Action Required: Please book your missing hours"

    # Test that the body contains all the correct, personalized info
    assert "Dear David Test" in body
    assert "for 11/2025" in body
    assert "are 160 hours" in body
    assert "you only book 100 hours" in body
