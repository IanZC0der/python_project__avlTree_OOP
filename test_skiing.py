# test the Skiing class. Enter "pytest test_skinng.py" to run the test

import skiing
import pytest


def test_constructor():
    """Test the constructor."""
    aSkiing = skiing.Skiing()
    assert aSkiing._when == ""
    assert aSkiing._location == ""
    assert aSkiing._size == 0
    assert aSkiing._equipment == []


def test_display(capfd):
    """test the display() method."""
    aSkiing = skiing.Skiing()
    aSkiing.display()
    out, err = capfd.readouterr()
    assert out == f"The event is taking place on {aSkiing._when}.\nThe event will be at {aSkiing._location}.\n{aSkiing._size} people will be attending this event.\nThe equipment list is: {aSkiing._equipment}.\n"


def test_inputData(monkeypatch):
    """test the inputData() method."""
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    equipment = "poles,shoes"
    variables = iter([when, location, size, equipment])
    monkeypatch.setattr('builtins.input', lambda _: next(variables))
    # reference: https://stackoverflow.com/questions/53472142/pytest-user-input-simulation
    aSkiing = skiing.Skiing()
    aSkiing.inputData()
    assert aSkiing._when == "20220809"
    assert aSkiing._location == "1988 SW Scot St"
    assert aSkiing._size == 2
    assert aSkiing._equipment == equipment.split(',')


def test_update():
    """Test the updateEqplist() method."""
    aSkiing = skiing.Skiing()
    equipment = "poles,shoes"
    aSkiing.updateEqplist(equipment.split(','))
    assert aSkiing._equipment == equipment.split(',')


def test_eq():
    """test the '==' operator."""
    aSkiing1 = skiing.Skiing()
    aSkiing2 = skiing.Skiing()
    assert (aSkiing1 == aSkiing2) == True
    aSkiing3 = skiing.Skiing("20220809", "1988 SW Scot St", "2", [
                             "shoes", "pole"])
    assert (aSkiing1 == aSkiing3) == False
