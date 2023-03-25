# test the Event module. Enter the command "pytest test_event.py" to run the test
import pytest
import event


def test_constructor():
    """test the constructor."""
    anEvent1 = event.Event()
    assert anEvent1._when == ""
    assert anEvent1._location == ""
    assert anEvent1._size == 0
    with pytest.raises(ValueError) as e_info:
        anEvent2 = event.Event("20220809", "1988 SW Scot St", "three")
    assert e_info.type is ValueError

    anEvent3 = event.Event("20220809", "1988 SW Scot St", 2)
    assert anEvent3._when == "20220809"
    assert anEvent3._location == "1988 SW Scot St"
    assert anEvent3._size == 2


def test_display(capfd):
    """test the display() method."""
    anEvent = event.Event()
    anEvent.display()
    out, err = capfd.readouterr()
    assert out == f"The event is taking place on {anEvent._when}.\nThe event will be at {anEvent._location}.\n{anEvent._size} people will be attending this event.\n"


def test_inputData(monkeypatch):
    """test the inputData() method."""
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    variables = iter([when, location, size])
    monkeypatch.setattr('builtins.input', lambda _: next(variables))
    # reference: https://stackoverflow.com/questions/53472142/pytest-user-input-simulation
    anEvent = event.Event()
    anEvent.inputData()
    assert anEvent._when == "20220809"
    assert anEvent._location == "1988 SW Scot St"
    assert anEvent._size == 2


def test_update():
    """test the updateLocation(location), updateWhen(when), updateSize(size) methods."""
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    anEvent = event.Event()
    anEvent.updateLocation(location)
    anEvent.updateWhen(when)
    anEvent.updateSize(size)
    assert anEvent._when == "20220809"
    assert anEvent._location == "1988 SW Scot St"
    assert anEvent._size == 2


def test_eq():
    """test the '==' operator."""
    anEvent1 = event.Event()
    anEvent2 = event.Event()
    assert (anEvent1 == anEvent2) == True
    anEvent3 = event.Event("20220809", "1988 SW Scot St", "2")
    assert (anEvent1 == anEvent3) == False
