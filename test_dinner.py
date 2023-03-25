# test the Dinner module. Enter "pytest test_dinner.py" to run the test
import pytest
import dinner


def test_constructor():
    """Test the constructor."""
    aDinner = dinner.Dinner()
    assert aDinner._when == ""
    assert aDinner._location == ""
    assert aDinner._size == 0
    assert aDinner._guestList == []
    assert aDinner._incentive == ""


def test_display(capfd):
    """test the display() method."""
    aDinner = dinner.Dinner()
    aDinner.display()
    out, err = capfd.readouterr()
    assert out == f"The event is taking place on {aDinner._when}.\nThe event will be at {aDinner._location}.\n{aDinner._size} people will be attending this event.\nThe guest list is {aDinner._guestList}.\nThe incentive is : {aDinner._incentive}.\n"


def test_inputData(monkeypatch):
    """test the inputData() method."""
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    guestList = "John,Giner"
    incentive = "birthday party"
    variables = iter([when, location, size, guestList, incentive])
    monkeypatch.setattr('builtins.input', lambda _: next(variables))
    # reference: https://stackoverflow.com/questions/53472142/pytest-user-input-simulation
    aDinner = dinner.Dinner()
    aDinner.inputData()
    assert aDinner._when == "20220809"
    assert aDinner._location == "1988 SW Scot St"
    assert aDinner._size == 2
    assert aDinner._guestList == guestList.split(',')
    assert aDinner._incentive == incentive


def test_update():
    """Test the updateGuestList() and updateIncentive() methods."""
    aDinner = dinner.Dinner()
    guestList = "John,Giner"
    incentive = "birthday party"
    aDinner.updateGuestList(guestList.split(','))
    aDinner.updateIncentive(incentive)
    assert aDinner._guestList == guestList.split(',')
    assert aDinner._incentive == incentive


def test_eq():
    """test the '==' operator."""
    aDinner1 = dinner.Dinner()
    aDinner2 = dinner.Dinner()
    assert (aDinner1 == aDinner2) == True
    aDinner3 = dinner.Dinner("20220809", "1988 SW Scot St", "2", [
                             "John", "Giner"], "birthday party")
    assert (aDinner1 == aDinner3) == False
