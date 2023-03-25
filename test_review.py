# Test the Review class
import review
import dinner
import skiing
import travel
import pytest


def test_constructor():
    """test the contructor."""
    aReview = review.Review()
    assert aReview._data == None
    assert aReview._comment == ""
    aTravel = travel.Travel()
    aReview2 = review.Review(aTravel, "test message")
    assert aReview2._data == aTravel
    assert aReview2._comment == "test message"


def test_display_no_data(capfd):
    """test the display function, no actual data."""
    aReview1 = review.Review()
    aReview1.display()
    out, err = capfd.readouterr()
    assert out == "NO DATA.\n"


def test_display_with_data(capfd):
    """test the display function, with data."""
    aTravel = travel.Travel()
    aReview = review.Review(aTravel, "test message")
    aReview.display()
    out, err = capfd.readouterr()
    assert out == f'The event is taking place on {aTravel._when}.\nThe event will be at {aTravel._location}.\n{aTravel._size} people will be attending this event.\nThe destination: {aTravel._country}.\nTransportation: {aTravel._transportation}.\nComment/Review: {aReview._comment}\n'


def test_enter_data_invalid_input(monkeypatch, capfd):
    """test the enterData() method with invalid input."""
    aReview = review.Review()
    command = "invalid"  # the command is invalid
    variables = iter([command])
    monkeypatch.setattr('builtins.input', lambda _: next(variables))
    aReview.enterData()
    out, err = capfd.readouterr()
    assert out == "Invalid input.\n"
    assert aReview._data == None
    assert aReview._comment == ""


def test_enter_data_valid_input1(monkeypatch):
    """test the enterData() method with valid input."""
    aReview = review.Review()
    command = 'T'  # the 'T' would be converted to 't'
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    country = "U.S."
    transportation = "car"
    comment = "test comment."
    aTravel = travel.Travel(when, location, size, country, transportation)
    inputList = iter([command, when, location, size,
                     country, transportation, comment])
    monkeypatch.setattr('builtins.input', lambda _: next(inputList))
    aReview.enterData()
    assert aReview._data == aTravel  # these two data should be the same
    assert aReview._comment == "test comment."


def test_enter_data_valid_input2(monkeypatch):
    """test the enterData() method with valid input."""
    aReview = review.Review()
    command = 'D'  # the 'D' would be converted to 'd'
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    guestList = "John,Giner"
    incentive = "birthday party"
    comment = "test comment."
    aDinner = dinner.Dinner(when, location, size,
                            guestList.split(','), incentive)
    inputList = iter([command, when, location, size,
                     guestList, incentive, comment])
    monkeypatch.setattr('builtins.input', lambda _: next(inputList))
    aReview.enterData()
    assert aReview._data == aDinner  # these two data should be the same
    assert aReview._comment == comment


def test_enter_data_valid_input3(monkeypatch):
    """test the enterData() method with valid input."""
    aReview = review.Review()
    command = 'S'  # the 'S' would be converted to 's'
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    equipment = "poles,shoes"
    comment = "test comment."
    aSkiing = skiing.Skiing(when, location, size,
                            equipment.split(','))
    inputList = iter([command, when, location, size,
                     equipment, comment])
    monkeypatch.setattr('builtins.input', lambda _: next(inputList))
    aReview.enterData()
    assert aReview._data == aSkiing  # these two data should be the same
    assert aReview._comment == comment


def test_updateData():
    """test eh updateDate() method with three different inputs."""
    when = "20220809"
    location = "1988 SW Scot St"
    size = "2"
    equipment = "poles,shoes"
    comment = "test comment."
    aSkiing = skiing.Skiing(when, location, size,
                            equipment.split(','))
    aReview = review.Review()
    aReview.updateData(aSkiing)  # update the member data with different data
    assert aReview._data == aSkiing
    guestList = "John,Giner"
    incentive = "birthday party"
    aDinner = dinner.Dinner(when, location, size,
                            guestList.split(','), incentive)
    aReview.updateData(aDinner)  # update the member data with different data
    assert aReview._data == aDinner
    country = "U.S."
    transportation = "car"
    aTravel = travel.Travel(when, location, size, country, transportation)
    aReview.updateData(aTravel)
    assert aReview._data == aTravel


def test_updateComment():
    """test the update comment method."""
    newComment = "test comment."
    aReview = review.Review()
    aReview.updateComment(newComment)
    assert aReview._comment == newComment


def test_lt_operator():
    """test the overloaded '<' operator."""
    firstString = "testa"
    secondString = "testb"
    aReview1 = review.Review(None, firstString)
    aReview2 = review.Review(None, secondString)
    assert (aReview1 < aReview2) == (firstString < secondString)
