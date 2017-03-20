#!/usr/bin/python

#######################################################################
#                                                                     #
# This class implements the interface for the collection class. This  #
# interface defines all the apis to be used by caller. None of these  #
# methods are implemented in this class. The class that derives from  #
# this class has to implement each method listed in this class.       #
#                                                                     #
#######################################################################


class ICollection:
    """
    Defines an interface for the collection class. Each class that 
    inherits from this class has to implement every method in this
    class.
    """
    # api to list all unique elements in the collection.
    def getUniqueItems(self):
        """
        This method should return a list of all unique elements in 
        this collection. This method needs to be overridden in the 
        derived class.
        """
        raise NotImplementedError

    def getItemsWithFrequency(self):
        """
        This method should return the list of items along with their
        frequency. This method should also needs to be overridden. 
        """
        raise NotImplementedError

    def insert(self, item):
        """
        This method inserts the item in the collection.
        item - Item to be inserted in the collection. Various data
               that can be passed are string, list, dict.
        """
        raise NotImplementedError
