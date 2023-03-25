# Implementing Dinner class
from event import Event


class Dinner(Event):
    def __init__(self, when="", location="", size=0, guestList=[], incentive=""):
        """default constructor."""
        super().__init__(when, location, size)
        self._guestList = guestList
        self._incentive = incentive

    def display(self):
        """display the data."""
        super().display()
        print(f'The guest list is {self._guestList}.')
        print(f'The incentive is : {self._incentive}.')

    def inputData(self):
        """prompt the client to enter the data."""
        super().inputData()
        inputList = input(
            "Please enter the guest list and seperate the names by ',' (e.g., Thomas Whitty, Ben Galler):\n")
        self._guestList = inputList.split(',')
        self._incentive = input("Please enter the incentive for this dinner:")

    def updateGuestList(self, guestList):
        """Update the guestlist."""
        self._guestList = guestList.copy()

    def updateIncentive(self, incentive):
        """update the incentive."""
        self._incentive = incentive

    def __eq__(self, aDinner):
        """overload the '==' operator."""
        if not isinstance(aDinner, Dinner):
            return False  # not an instance of Dinner class, return false
        return super().__eq__(aDinner) and self._guestList == aDinner._guestList and self._incentive == aDinner._incentive
