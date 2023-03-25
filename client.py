# client methods
import dinner
import skiing
import travel
import review
import all


def enterCommand():
    """prompt the user to enter a command."""
    aCommand = input("Please enter a command: ").lower()
    return aCommand


def displayMenu():
    """display the menu."""
    print("Welcome to MyEvents 1.0:\n\
        \ta. display all the events to be attended\n\
        \tb. add new data to the events\n\
        \tc. display the reviews\n\
        \td. retrieve data according to the review\n\
        \te. insert new data to the reviews\n\
        \tq. quit\n")


def retrieveData(anAvl):
    """retrieve data from an AVL Tree."""
    review = input("Please enter a review:")
    aReview = anAvl.retrieve(review)
    if not aReview:
        # the method returns None if no match is found
        print("No matched data.")
    else:
        print("One match found:")
        aReview.display()


def insertToReviews(anAvl):
    """insert new data to the reviews."""
    aReview = review.Review()
    aReview.enterData()
    print("The new review data is:")
    print()
    aReview.display()
    newAvl = anAvl.insert(aReview)
    print("Insertion successful!")
    return newAvl


def executeCommand(aCommand, anAll, anAvl):
    """execute the command."""
    if aCommand == 'a':
        anAll.display()
        return anAll
    elif aCommand == 'b':
        newAll = anAll.enterData()
        return newAll
    elif aCommand == 'c':
        anAvl.display()
        return anAvl
    elif aCommand == 'e':
        newAvl = insertToReviews(anAvl)
        return newAvl
    elif aCommand == 'd':
        retrieveData(anAvl)
        return anAvl
    else:
        print("Invalid command!")
        return anAll
