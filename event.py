# Implementing the base class 'Event'
class Event:
    def __init__(self, when="", aLocation="", size=0):
        """default constructor."""
        self._when = when  # the data on which the event takes place
        self._location = aLocation  # the location at which the event takes place
        # the number of people who are attending the event
        self._size = int(size)

    def display(self):
        """display the object."""
        print(f'The event is taking place on {self._when}.')
        print(f'The event will be at {self._location}.')
        print(f'{self._size} people will be attending this event.')

    def inputData(self):
        """prompt the user to enter the data."""
        self._when = input("Please enter the date: ")
        self._location = input("Please enter the location: ")
        self._size = int(input("Please enter the number of people: "))

    def updateWhen(self, when):
        """update the attribute."""
        self._when = when

    def updateLocation(self, location):
        """update the attribute."""
        self._location = location

    def updateSize(self, size):
        """update the attribute."""
        self._size = int(size)

    def __eq__(self, anEvent):
        """overload the equality operator."""
        return self._when == anEvent._when and self._location == anEvent._location and self._size == anEvent._size
