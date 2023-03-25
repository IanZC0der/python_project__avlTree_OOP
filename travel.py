# Implementing the Travel class
from event import Event


class Travel(Event):
    def __init__(self, when="", aLocation="", size=0, country="", transportation=""):
        """constructor."""
        super().__init__(when, aLocation, size)
        self._country = country
        self._transportation = transportation

    def display(self):
        """display the object."""
        super().display()
        print(f'The destination: {self._country}.')
        print(f'Transportation: {self._transportation}.')

    def inputData(self):
        """prompt the client to enter the data."""
        super().inputData()
        self._country = input(
            "Please enter your destination (a Country, e.g., Mexico): ")
        self._transportation = input("Please enter your transportation: ")

    def updateCountry(self, country):
        """update the data member '_country'"""
        self._country = country

    def updateTransportation(self, transportation):
        """update the data member '_transportation'"""
        self._transportation = transportation

    def __eq__(self, aTravel):
        """overload the '==' operator."""
        if not isinstance(aTravel, Travel):
            return False
        return super().__eq__(aTravel) and self._country == aTravel._country and self._transportation == self._transportation
