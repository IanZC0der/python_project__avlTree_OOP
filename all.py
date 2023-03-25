# Implementing the 'Node' class and the 'ALL' class
from dinner import Dinner
from skiing import Skiing
from travel import Travel
import sys


class Node:
    def __init__(self, aData=None):
        """Constructor."""
        self._data = aData
        self._next = None

    def setNext(self, next):
        """set the next node."""
        self._next = next

    def getNext(self):
        """get the next node."""
        return self._next

    def ifEqual(self, aData):
        """check if the data in the node is the same as aData."""
        if not self._data:
            return False
        return self._data == aData

    def display(self):
        """display the data in the node."""
        if self._data:
            self._data.display()


class ALL:
    def __init__(self):
        """constructor."""
        self._all = [None, None, None]  # a list that saves three LLLs

    def _display(self, aHead):
        """display the LLL recursively."""
        if not aHead:
            return
        aHead.display()  # invode display method in the Node class
        print()
        self._display(aHead.getNext())

    def display(self):
        """Display the ALL."""
        if not self._all[0] and not self._all[1] and not self._all[2]:
            print("NO DATA.")  # the ALL is empty
            return
        print("Dinner Events:")
        self._display(self._all[0])  # the first LLL saves the Dinner objects
        print("Skiing:")
        self._display(self._all[1])  # the second LLL saves the Skiing objects
        print("Travel:")
        self._display(self._all[2])  # the last LLL saves the Travel objects

    def _ifMatch(self, aHead, aData):
        """check if there is a match in the LLL."""
        if not aHead:
            return False
        if aHead.ifEqual(aData):
            return True
        return self._ifMatch(aHead.getNext(), aData)

    def __iadd__(self, aData):
        """overload the '+=' operator."""
        if isinstance(aData, Dinner):
            if not self._ifMatch(self._all[0], aData):
                # add the object to the corresponding LLL.
                self._all[0] = self._append(self._all[0], aData)
        elif isinstance(aData, Skiing):
            if not self._ifMatch(self._all[1], aData):
                self._all[1] = self._append(self._all[1], aData)
        elif isinstance(aData, Travel):
            if not self._ifMatch(self._all[2], aData):
                self._all[2] = self._append(self._all[2], aData)
        return self

    def _append(self, aHead, aData):
        """Add the data to the LLL recursively."""
        if not aHead:
            aHead = Node(aData)
            return aHead
        aHead.setNext(self._append(aHead.getNext(), aData))
        return aHead

    def enterData(self):
        """prompt the user to enter the data."""
        aType = input(
            "what kind of event? d for dinner, s for skiing, t for travel").lower()
        if aType == 'd':
            aDinner = Dinner()
            aDinner.inputData()
            self += aDinner
        elif aType == 's':
            aSkiing = Skiing()
            aSkiing.inputData()
            self += aSkiing
        elif aType == 't':
            aTravel = Travel()
            aTravel.inputData()
            self += aTravel
        else:
            print("Please check your input and retry.")
        return self

    def loadFromFile(self, fileName):
        """load data from a file."""
        try:
            f = open(fileName, 'r')  # open the file
        except OSError:
            sys.exit(f'Failed to open the file {fileName}.')
        with f:
            line = f.readline().rstrip('\n')  # read the line the delete the '\n'
            while line:
                # the first character in the line denotes the type of the object
                variableList = line.split(',')
                if line[0] == 'd':
                    aDinner = Dinner(variableList[1], variableList[2], int(
                        variableList[3]), variableList[4].split(';'), variableList[5])
                    self += aDinner
                elif line[0] == 's':
                    aSkiing = Skiing(variableList[1], variableList[2], int(
                        variableList[3]), variableList[4].split(';'))
                    self += aSkiing
                elif line[0] == 't':
                    aTravel = Travel(variableList[1], variableList[2], int(
                        variableList[3]), variableList[4], variableList[5])
                    self += aTravel
                line = f.readline().rstrip('\n')
        f.close()
