icollection.py
This file define the class ICollection. This class lists all the required
methods for the collection class. This is an analogous to the interface in 
java. This file does not have any implementation but only lists the methods.

collection.py
This file inherits from the ICollection class. In java analogy, it implements
the ICollection interface. This structure gives a neat understanding of methods
to be exposed for public usage. This class defines the functionality for 
each of the methods in ICollection and also implements any private methods.

test.py
This script instantiates the collection class and runs some test runs for each
method.

###############################################################################
To run the test run.
python test.py

The required methods are listed below.
1. def getUniqueItems(self):
    """
    This method should return a list of all unique elements in 
    this collection. This method needs to be overridden in the 
    derived class.
    """

2. def getItemsWithFrequency(self):
    """
    This method should return the list of items along with their
    frequency. This method should also needs to be overridden. 
    """

3. def insert(self, item):
    """
    This method inserts the item in the collection.
    item - Item to be inserted in the collection. Various data
           that can be passed are string, list, dict.
    """
