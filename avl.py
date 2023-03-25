# Implementing the AVLTree class
import review
from dinner import Dinner
from skiing import Skiing
from travel import Travel


class treeNode:
    def __init__(self, aData=None):
        self.data = aData
        self.left = None
        self.right = None
        self.height = 1  # initialize the height to be 1


class AVLTree:
    def __init__(self):
        """constructor."""
        self._root = None

    def insert(self, aData):
        """insert new data."""
        self._root = self._insert(self._root, aData)
        return self

    def _insert(self, root, aData):
        """recursively insert the new data."""
        if not root:
            return treeNode(aData)
        elif aData < root.data:
            # insert the new data to the left of the root
            root.left = self._insert(root.left, aData)
        else:
            # insert the new data to the right of the root
            root.right = self._insert(root.right, aData)
        # update the height of the root
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        # get the balance factor and rotate the tree if necessary
        bf = self.getBalanceFactor(root)
        if bf > 1:
            # bf > 1 means that the height of the left sub tree is greater than the right subtree and the current tree is unbalanced
            if aData < root.left.data:
                # perform right rotation if the new data is in the left subtree of the left child node
                return self.rightRotate(root)
            else:
                # perform left-right rotation if the new data is in the right subtree of the left child node
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if bf < -1:
            # bf < 1 means that the height of the right sub tree is greater than the left subtree and current tree is unbalanced
            if aData > root.right.data:
                # perform left rotation if the new data is in the right subtree of the right child node
                return self.leftRotate(root)
            else:
                # perform right-left rotation if the new data is in the left subtree of the right child node
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root  # current tree is balanced, no rotation

    def leftRotate(self, root):
        """perform left rotation."""
        newRoot = root.right  # initialize a new root
        hold = newRoot.left
        newRoot.left = root  # update the new root's left child node
        root.right = hold  # update the old root's right child node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))  # update height
        newRoot.height = 1 + \
            max(self.getHeight(newRoot.left), self.getHeight(
                newRoot.right))  # update height

        return newRoot

    def rightRotate(self, root):
        """perform right rotation."""
        newRoot = root.left  # initialize a new root
        hold = newRoot.right
        newRoot.right = root  # update the new root's right child node
        root.left = hold  # update the old root's left child node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))  # update height
        newRoot.height = 1 + \
            max(self.getHeight(newRoot.left), self.getHeight(
                newRoot.right))  # update height

        return newRoot

    def getHeight(self, root):
        """get the height of the current node."""
        if not root:
            return 0
        return root.height

    def getBalanceFactor(self, root):
        """get the balance facotor."""
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def display(self):
        """diaplay the whole tree."""
        if not self._root:
            print("NO DATA.")
            return
        self._display(self._root)

    def _display(self, root):
        """helper method that displays the tree recursively."""
        if root:
            self._display(root.left)
            root.data.display()
            print('\n')
            self._display(root.right)

    def retrieve(self, comment):
        """retrieve an object."""
        return self._retrieve(self._root, comment)

    def _retrieve(self, root, comment):
        """retrieve the object recursively. the comment is the search key."""
        if not root:
            return root
        aReview = review.Review(None, comment)
        if root.data == aReview:
            return root.data
        if aReview < root.data:
            return self._retrieve(root.left, comment)
        return self._retrieve(root.right, comment)

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
                    aReview = review.Review(aDinner, variableList[6])
                    self = self.insert(aReview)
                elif line[0] == 's':
                    aSkiing = Skiing(variableList[1], variableList[2], int(
                        variableList[3]), variableList[4].split(';'))
                    aReview = review.Review(aSkiing, variableList[5])
                    self = self.insert(aReview)
                elif line[0] == 't':
                    aTravel = Travel(variableList[1], variableList[2], int(
                        variableList[3]), variableList[4], variableList[5])
                    aReview = review.Review(aTravel, variableList[6])
                    self = self.insert(aReview)
                line = f.readline().rstrip('\n')
        f.close()
