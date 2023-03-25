# test the AVLtree
import review
import dinner
import skiing
import travel
import pytest
import avl


def test_constructor():
    anAvl = avl.AVLTree()
    anAvl._root == None


def test_rotate1():
    """test the left-right rotation."""
    anAvl = avl.AVLTree()
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    aReview1 = review.Review(aTravel, 9)
    aReview2 = review.Review(aDinner, 7)
    aReview3 = review.Review(aSkiing, 8)
    anAvl = anAvl.insert(aReview1)
    anAvl = anAvl.insert(aReview2)
    anAvl = anAvl.insert(aReview3)
    # assert the data objects are not modified and rotation is performed
    assert anAvl._root.data == aReview3
    assert anAvl._root.data._data == aReview3._data
    assert anAvl._root.left.data == aReview2
    assert anAvl._root.left.data._data == aReview2._data
    assert anAvl._root.right.data == aReview1
    assert anAvl._root.right.data._data == aReview1._data
    # assert that the height is correct
    assert anAvl.getHeight(anAvl._root) == 2
    assert anAvl.getHeight(anAvl._root.left) == 1
    assert anAvl.getHeight(anAvl._root.right) == 1
    # assert that the balance facotr is correct
    assert anAvl.getBalanceFactor(anAvl._root) == 0
    assert anAvl.getBalanceFactor(anAvl._root.left) == 0
    assert anAvl.getBalanceFactor(anAvl._root.right) == 0


def test_rotate2():
    """test the right-left rotation."""
    anAvl = avl.AVLTree()
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    aReview1 = review.Review(aTravel, 7)
    aReview2 = review.Review(aDinner, 9)
    aReview3 = review.Review(aSkiing, 8)
    anAvl = anAvl.insert(aReview1)
    anAvl = anAvl.insert(aReview2)
    anAvl = anAvl.insert(aReview3)
    # assert the data objects are not modified and rotation is performed
    assert anAvl._root.data == aReview3
    assert anAvl._root.data._data == aReview3._data
    assert anAvl._root.left.data == aReview1
    assert anAvl._root.left.data._data == aReview1._data
    assert anAvl._root.right.data == aReview2
    assert anAvl._root.right.data._data == aReview2._data
    # assert that the height is correct
    assert anAvl.getHeight(anAvl._root) == 2
    assert anAvl.getHeight(anAvl._root.left) == 1
    assert anAvl.getHeight(anAvl._root.right) == 1
    # assert that the balance facotr is correct
    assert anAvl.getBalanceFactor(anAvl._root) == 0
    assert anAvl.getBalanceFactor(anAvl._root.left) == 0
    assert anAvl.getBalanceFactor(anAvl._root.right) == 0


def test_retrieve_emptyAvl():
    """test retireving in an empty tree."""
    anAvl = avl.AVLTree()
    retrieved = anAvl.retrieve("nothing")
    assert retrieved == None


def test_retireve_nonEmpty():
    """test retrieving in a non-empty tree."""
    anAvl = avl.AVLTree()
    aTravel = travel.Travel()
    aSkiing = skiing.Skiing()
    aDinner = dinner.Dinner()
    aReview1 = review.Review(aTravel, 7)
    aReview2 = review.Review(aDinner, 9)
    aReview3 = review.Review(aSkiing, 8)
    anAvl = anAvl.insert(aReview1)
    anAvl = anAvl.insert(aReview2)
    anAvl = anAvl.insert(aReview3)
    retrived = anAvl.retrieve(9)
    assert retrived == aReview2  # matched
    retrieved2 = anAvl.retrieve(1)
    assert retrieved2 == None  # no match


def test_loadData_valid():
    """test the loadDataFromFile() method."""
    anAvl = avl.AVLTree()
    anAvl.loadFromFile("review.txt")  # load data
    # assert the tree is a balanced tree after loading the data
    anAvl._root.data._comment == "it would be more fun if there are more friends coming."
    anAvl._root.left.data._comment == "a little too far."
    anAvl._root.left.right.data._comment == "could visit a friend in Seatle next time."
    anAvl._root.right.data._comment == "we need better food."
    anAvl._root.right.left.data._comment == "should have brought a better present."
    anAvl._root.right.right.data._comment == "will not go to Paris in the future."
