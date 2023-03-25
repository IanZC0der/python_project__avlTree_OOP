# test the Travel class. Enter "pytest test_travel.py" to run the test
import travel
import pytest


def test_constructor():
    """Test the constructor."""
    aTravel = travel.Travel()
    assert aTravel._when == ""
    assert aTravel._location == ""
    assert aTravel._size == 0
    assert aTravel._country == ""
    assert aTravel._transportation == ""


def test_display(capfd):
    """test the display() method."""
    aTravel = travel.Travel()
    aTravel.display()
    out, err = capfd.readouterr()
    assert out == f"The event is taking place on {aTravel._when}.\nThe event will be at {aTravel._location}.\n{aTravel._size} people will be attending this event.\nThe destination: {aTravel._country}.\nTransportation: {aTravel._transportation}.\n"


def test_inputData(monkeypatch):
    """test the inputData() method."""
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    country = "U.S."
    transportation = "car"
    variables = iter([when, location, size, country, transportation])
    monkeypatch.setattr('builtins.input', lambda _: next(variables))
    # reference: https://stackoverflow.com/questions/53472142/pytest-user-input-simulation
    aTravel = travel.Travel()
    aTravel.inputData()
    assert aTravel._when == "20220809"
    assert aTravel._location == "1988 SW Scot St"
    assert aTravel._size == 2
    assert aTravel._country == "U.S."
    assert aTravel._transportation == "car"


def test_update():
    """Test the updateCountry() and updateTransportation() method."""
    aTravel = travel.Travel()
    country = "U.S."
    transportation = "car"
    aTravel.updateCountry(country)
    aTravel.updateTransportation(transportation)
    assert aTravel._country == "U.S."
    assert aTravel._transportation == "car"


def test_eq():
    """test the '==' operator."""
    aTravel1 = travel.Travel()
    aTravel2 = travel.Travel()
    assert (aTravel1 == aTravel2) == True
    aTravel3 = travel.Travel("20220809", "1988 SW Scot St", "2", "U.S.", "car")
    assert (aTravel1 == aTravel3) == False
