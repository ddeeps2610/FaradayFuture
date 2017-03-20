#!/usr/bin/python

#####################################################################
#                                                                   #
# This file instantiates the collection and tests various apis.     #
#                                                                   #
#####################################################################


# Import statements
from collection import Collection

coll = Collection()

# Insert elements
coll.insert('television')
coll.insert(['printer', 'xbox', 'chair', 'table', 'chair'])
coll.insert({'speaker':2, 'couch':1, 'shoes':4})

# Print unique elements.
print coll.getUniqueItems()

# Print all elements along with their counts.
print coll.getItemsWithFrequency()
