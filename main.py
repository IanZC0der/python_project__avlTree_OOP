# enter "python3 main.py" to run the program
from dinner import Dinner
import event
from travel import Travel
from skiing import Skiing
import review
import avl
import all
import client


def main():
    anAll = all.ALL()
    anAll.loadFromFile("data.txt")  # load data from file
    anAvl = avl.AVLTree()
    anAvl.loadFromFile("review.txt")  # load data from file
    client.displayMenu()
    aCommand = client.enterCommand()
    while aCommand != 'q':
        # this function needs to return an updated object because the arguments are passed by value
        returnObject = client.executeCommand(aCommand, anAll, anAvl)
        if isinstance(returnObject, all.ALL):
            anAll = returnObject  # update anAll
        if isinstance(returnObject, avl.AVLTree):
            anAvl = returnObject  # update anAvl
        client.displayMenu()
        aCommand = client.enterCommand()


if __name__ == "__main__":
    main()
