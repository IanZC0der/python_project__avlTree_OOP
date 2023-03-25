# Test the ALL class
import all
import travel
import skiing
import dinner
import pytest


def test_NodeConstructor():
    """Test the Node class constructor."""
    newNode1 = all.Node()
    assert newNode1._data == None
    assert newNode1._next == None


def test_Nodenext():
    """Test the getNext() and setNext() methods."""
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    newNode2 = all.Node(aTravel)
    newNode3 = all.Node(aSkiing)
    newNode4 = all.Node(aDinner)
    newNode2.setNext(newNode3)
    newNode3.setNext(newNode4)
    assert newNode2.getNext() == newNode3
    assert newNode3.getNext() == newNode4


def test_NodeifEqual():
    """test the ifEqual() method."""
    aTravel1 = travel.Travel()
    aTravel2 = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    newNode = all.Node(aTravel1)
    assert newNode.ifEqual(aTravel2) == True
    # comparing objects of different types, return false
    assert newNode.ifEqual(aSkiing) == False
    assert newNode.ifEqual(aDinner) == False


def test_Node_display_None(capfd):
    """Test the display method in the Node class. Nothing should be printed if there is no data in the Node."""
    newNode = all.Node()
    newNode.display()
    out, err = capfd.readouterr()
    assert out == ""


def test_Node_display_NotNone(capfd):
    """Test the display method in the Node class."""
    """display the data if there is a piece of data in the node."""
    aDinner = dinner.Dinner()
    newNode = all.Node(aDinner)
    newNode.display()
    out, err = capfd.readouterr()
    assert out == f"The event is taking place on {aDinner._when}.\nThe event will be at {aDinner._location}.\n{aDinner._size} people will be attending this event.\nThe guest list is {aDinner._guestList}.\nThe incentive is : {aDinner._incentive}.\n"


def test_all_constructor():
    """Test the ALL constructor."""
    aList = [None, None, None]
    # The constructor should should create a list that contains None as placeholders
    anAll = all.ALL()
    assert anAll._all == aList


def test_all_display_helper_None(capfd):
    """Test the _display method is the ALL class."""
    anAll = all.ALL()
    anAll._display(None)  # display nothing
    out, err = capfd.readouterr()
    assert out == ""


def test_all_display_helper_NotNone(capfd):
    """Test the _display method in the ALL class."""
    """print the contents recursively in the LLL."""
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    newNode1 = all.Node(aTravel)
    newNode2 = all.Node(aSkiing)
    newNode3 = all.Node(aDinner)
    newNode1.setNext(newNode2)
    newNode2.setNext(newNode3)  # create a linear linked list
    anAll = all.ALL()
    anAll._display(newNode1)
    out, err = capfd.readouterr()
    assert out == f"The event is taking place on {aTravel._when}.\nThe event will be at {aTravel._location}.\n{aTravel._size} people will be attending this event.\nThe destination: {aTravel._country}.\nTransportation: {aTravel._transportation}.\n\nThe event is taking place on {aSkiing._when}.\nThe event will be at {aSkiing._location}.\n{aSkiing._size} people will be attending this event.\nThe equipment list is: {aSkiing._equipment}.\n\nThe event is taking place on {aDinner._when}.\nThe event will be at {aDinner._location}.\n{aDinner._size} people will be attending this event.\nThe guest list is {aDinner._guestList}.\nThe incentive is : {aDinner._incentive}.\n\n"


def test_all_display_no_data(capfd):
    """Test the display method in the ALL class."""
    """The message 'NO DATA.' is displayed if there is no data."""
    anAll = all.ALL()
    anAll.display()
    out, err = capfd.readouterr()
    assert out == "NO DATA.\n"


def test_all_display_have_data(capfd):
    """Test the display method in the ALL class."""
    """print all the data in the ALL."""
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    newNode1 = all.Node(aTravel)
    newNode2 = all.Node(aSkiing)
    newNode3 = all.Node(aDinner)
    aList = [newNode3, newNode2, newNode1]  # three LLLs.
    anAll = all.ALL()
    # change the private data directly. The operation is for testing only.
    anAll._all = aList
    anAll.display()
    out, err = capfd.readouterr()
    assert out == f"Dinner Events:\nThe event is taking place on {aDinner._when}.\nThe event will be at {aDinner._location}.\n{aDinner._size} people will be attending this event.\nThe guest list is {aDinner._guestList}.\nThe incentive is : {aDinner._incentive}.\n\nSkiing:\nThe event is taking place on {aSkiing._when}.\nThe event will be at {aSkiing._location}.\n{aSkiing._size} people will be attending this event.\nThe equipment list is: {aSkiing._equipment}.\n\nTravel:\nThe event is taking place on {aTravel._when}.\nThe event will be at {aTravel._location}.\n{aTravel._size} people will be attending this event.\nThe destination: {aTravel._country}.\nTransportation: {aTravel._transportation}.\n\n"


def test_ifMatch():
    """Test the _ifMatch() method in the ALL class."""
    anAll = all.ALL()
    aTravel = travel.Travel()
    newNode = all.Node(aTravel)
    # the head the the LLL is None, return False
    assert anAll._ifMatch(None, aTravel) == False
    # Note that _ifMatch() is a private method in the ALL class
    # "newNode" is a imaginary LLL that should have been in the ALL.
    assert anAll._ifMatch(newNode, aTravel) == True
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    newNode1 = all.Node(aTravel)
    newNode2 = all.Node(aSkiing)
    newNode3 = all.Node(aDinner)
    newNode1.setNext(newNode2)
    newNode2.setNext(newNode3)
    # set up a LLL that contains three pieces of data
    assert anAll._ifMatch(newNode1, aSkiing) == True
    assert anAll._ifMatch(newNode1, aDinner) == True


def test_append():
    """Test the _append() method in the ALL class."""
    anAll = all.ALL()
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    aHead = None
    aHead = anAll._append(aHead, aTravel)  # add data to the LLL
    assert aHead._data == aTravel
    aHead = anAll._append(aHead, aSkiing)  # add data to the LLL
    assert aHead._next._data == aSkiing


def test_operator_overloaded():
    """Test the '+=' operator in the ALL class."""
    anAll = all.ALL()
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    anAll += aDinner  # add data to the ALL
    anAll += aSkiing
    anAll += aTravel
    # the first LLL is for 'Dinner' objects
    assert anAll._all[0]._data == aDinner
    # the second LLL is for 'Skiing' objects
    assert anAll._all[1]._data == aSkiing
    # the third LLL is for 'Travel' objects
    assert anAll._all[2]._data == aTravel
    anAll += aDinner  # add the same data one more time. The repeated data should not be added
    anAll += aSkiing
    anAll += aTravel
    assert anAll._all[0]._next == None
    assert anAll._all[1]._next == None
    assert anAll._all[2]._next == None


def test_loadFromFile_invalid_fileName():
    """Test the loadFromFile() method in the ALL class."""
    """The fileName in this test case is invalid."""
    anAll = all.ALL()
    with pytest.raises(SystemExit) as e:
        anAll.loadFromFile("invalid.txt")
    assert e.type == SystemExit
    assert str(e.value) == "Failed to open the file invalid.txt."


def test_read_from_file_validFile():
    """Test the loadFromFile() method in the ALL class."""
    """The fileName in this case is valid."""
    anAll = all.ALL()
    anAll.loadFromFile("data.txt")
    aList1 = "John;Grace;Me"
    # create objects using the same data in the file
    aDinner = dinner.Dinner("20221214", "3025 SW Canby St Portland",
                            "3", aList1.split(';'), "John's graduation")
    aList2 = "Chris;Joe;Ellen;Me"
    aDinner2 = dinner.Dinner(
        "20221225", "6319 SW Capitol Hwy Portland", "4", aList2.split(';'), "Christmas")
    # verify the added data
    assert anAll._all[0]._data == aDinner
    assert anAll._all[0]._next._data == aDinner2
    assert anAll._all[0]._next._next == None

    aList3 = "skis/snowboard;boots;poles"
    aSkiing1 = skiing.Skiing(
        "20221216", "Mt. Bachelor OR", "2", aList3.split(';'))
    aSkiing2 = skiing.Skiing(
        "20221223", "Mt. Hood Meadows OR", "4", aList3.split(';'))
    assert anAll._all[1]._data == aSkiing1
    assert anAll._all[1]._next._data == aSkiing2
    assert anAll._all[1]._next._next == None

    aTravel1 = travel.Travel(
        "20230210", "Pl. du Louvre Paris", "2", "France", "Flight")
    aTravel2 = travel.Travel(
        "20230102", "Seatle Washington", "2", "U.S.", "Road trip")
    assert anAll._all[2]._data == aTravel1
    assert anAll._all[2]._next._data == aTravel2
    assert anAll._all[2]._next._next == None
