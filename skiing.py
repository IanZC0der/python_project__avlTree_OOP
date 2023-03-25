# Implementing the Skiing class
from event import Event


class Skiing(Event):
    def __init__(self, when="", location="", size=0, equipment=[]):
        """default constructor."""
        super().__init__(when, location, size)
        self._equipment = equipment.copy()

    def display(self):
        """display the object."""
        super().display()
        print(f'The equipment list is: {self._equipment}.')

    def inputData(self):
        """prompt the client to enter the data."""
        super().inputData()
        inputList = input(
            "Please enter the equipment list and seperate the item by ',' (e.g., board, shoes):\n")
        self._equipment = inputList.split(',')

    def updateEqplist(self, aList):
        """update the equipment list."""
        self._equipment = aList.copy()

    def __eq__(self, aSkiing):
        """overload the '==' operator."""
        if not isinstance(aSkiing, Skiing):
            return False  # not an instance of Skiing class, return false
        return super().__eq__(aSkiing) and self._equipment == aSkiing._equipment
