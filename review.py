# Implementing the review class
import dinner
import skiing
import travel


class Review:
    def __init__(self, aData=None, aReview=""):
        """constructor."""
        self._data = aData  # the data is a Dinner/Skiing/Travel object
        self._comment = aReview  # a string

    def display(self):
        """display the data."""
        if not self._data:
            print("NO DATA.")
            return
        self._data.display()
        print(f"Comment/Review: {self._comment}")

    def enterData(self):
        """prompt the user to enter a new object."""
        aData = None
        command = input(
            "Please indicate the type of the event: d for dinner, s for skking, t for travel").lower()
        if command == 'd':
            aDinner = dinner.Dinner()
            aDinner.inputData()
            aData = aDinner
        elif command == 's':
            aSkiing = skiing.Skiing()
            aSkiing.inputData()
            aData = aSkiing
        elif command == 't':
            aTravel = travel.Travel()
            aTravel.inputData()
            aData = aTravel
        else:
            print("Invalid input.")
            return
        self._comment = input("Please enter the review:")
        self._data = aData

    def updateData(self, aData):
        """update the data member."""
        self._data = aData

    def updateComment(self, aComment):
        """update the comment."""
        self._comment = aComment

    def __lt__(self, aReview):
        """overload the '<' operator."""
        return self._comment < aReview._comment

    def __eq__(self, aReview):
        """overload the '==' operator."""
        return self._comment == aReview._comment
