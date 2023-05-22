# Python Project Implementing AVL Tree with OOP Applied


## Topics
- Pytest
- [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree)
- Inheritance in Python

## Introduction

This project was the last assignment of [CS302](http://web.cecs.pdx.edu/~karlaf/CS302%20Flyer.html) at [PSU](https://www.pdx.edu/), designed by [Karla Fant](http://web.cecs.pdx.edu/~karlaf/), a great instructor at PSU, for the course CS302, titled [Programming Methodologies and Software 
implementation](http://web.cecs.pdx.edu/~karlaf/CS302%20Flyer.html), in which we practiced OOP with CPP and Python. In this assignment we implemented [AVL tree](https://en.wikipedia.org/wiki/AVL_tree) in Python and practiced OOP in python as well. What was featured in this project is that we also used the pytest 
framework to test our program. Specifically, we performed unit tests on each of the class we implemented.


Here we were asked to keep track of different sorts of "events" (e.g., travel plan, dinner, vacation plan) that we choose. Also, we need to enable the clients to review the events they have planned/participated. 


## Inheritance Relationship and Data Structures


This is a fairly simple program in terms of the inheritance relationship, which is Event->Dinner/Skiing/Travel. Also, a "Review" class was created to provide the review functionality. An instance of the Review class contains a Dinner/Skiing/Travel object. We were asked to create an array of linear linked lists to save the Dinner/Skiing/Travel objects and an AVL tree to save the Review objects. In my implementation, I created an array of three linear linked lists, each of which saves objects of different types for the convenience of searching. Notice that in reality the use of data structures should serve the algorithm. In this project, these two data structures are forced to implemented for practice.


The basic structures of the three derived classes are quite similar. Methods that allow the client to get, update and compare the objects. In the Review class the "<" operator was overloaded as the objects were saved in AVL tree and these objects need to be sorted. 



## Review


### "One bug"

when I was working on this project I was still transitioning to Python from C++. One of the major differences of these two languages is that Python does not support pass 
by reference in the functions. Thus, if we want to update an object, we can just pass it by reference in C++ and update it without returning anything. However, this does not work for Python. When I first passed the parameters to the function at line 22 in `main.py`, I didn't have the function return anything. And whenever I updated the objects, it didn't "actually" get updated. It troubled me for a while because I had been used to thinking of passing by reference until I realized that I needed to return the updated objects. Since I used an AVL tree object and an array of linear linked lists object, I had to use the `isinstance()` function to see which object could get updated at line 23 and 25 in `main.py`. Whereras in C++, this extra piece of code could be unnecessary.




