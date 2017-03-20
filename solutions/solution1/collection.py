#/usr/bin/python

###################################################################
#                                                                 #
# Problem Statement:                                              #
# 1. Write a new class with the following requirements            #
#    a. To store a list of items                                  #
#    b. A method to return all unique items from the list         #
#    c. A method to return all iterms and their frequency         #
#    d. Should be able to append/insert new iterms to the list    # 
###################################################################


###################################################################
# Solution
###################################################################
# Import statements
import logging
from icollection import ICollection


class Collection(ICollection):
    """
    Defines a class that stores list of all items and provides 
    various APIs to access or operate on the items.
    """
    items = None
    def __init__(self):
        """
        Initializes the data structure.
        """
        logging.info('Grocery store is initialized')
        self.items = dict()


    def getUniqueItems(self):
        """
        Returns a list of all unique items in the list.
        """
        logging.info('Requesting Unique Items')
        return self.items.keys()

   
    def getItemsWithFrequency(self):
        """
        Returns list of tuples one for each item type. The tuple is 
        in the form (<item>, <frequency>).
        If there are no items, it returns an empty list. 
        """ 
        itemFreqList = list()      
        for item, count in self.items.iteritems():
            itemFreqList.append((item, count))
        return itemFreqList


    def insertItem(self, item, count=1):
        """
        Inserts a single item.
        item - single item
        """
        if item:
            if item in self.items.keys():
                self.items[item] += count
            else:
                self.items[item] = count
        return True


    def insertItemsFromList(self, items):
        """
        Inserts list of items. 
        items - list of items to be inserted.
        Returns True if successfully inserted.
        """
        if items:
            for item in items:
                self.insertItem(item)
        return True
    

    def insertItemsFromDict(self, items):
        """
        Inserts items from a dictionary. Each entry in the dictionary 
        is in the form of {item: count}.
        """
        if items:
            for item, count in items.iteritems():
                if count > 0:
                    self.insertItem(item, count)
        return True

    def insert(self, item):
        """
        Depending on the type of item, insert the item in the registry.
        """
        result = False
        if type(item) == str:
            result = self.insertItem(item)
        elif type(item) == list:
            result = self.insertItemsFromList(item)
        elif type(item) == dict:
            result = self.insertItemsFromDict(item)
        else:
            logging.info('Unknown type: {}'.format(type(item)))
            result = False
        return result
