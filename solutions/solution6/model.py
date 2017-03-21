#!/usr/bin/env python

import random
import json
import os

class Model(object):
    """
    Class to define the underlying model of the data.
    """
    def __init__(self, datafile):
        """
        Loads the data set from the datafile-ca.json.
        datafile - json dump file that contains the city information
        Note: There are 489 entries in total out of which 2 are duplicates.
        So, when loading, duplicate entries are removed. As such, there are 
        487 enties in the model dataset.
        """
        if os.path.exists(datafile) and os.path.isfile(datafile):
            fp = open(datafile, 'rb+')
            self.cities = json.loads(fp.read())
            fp.close()
            self.cityInfo = dict()
            self.loadData()
            del self.cities 

    def loadData(self):
        """
        Loads the data into the dictionary for quick reference.
        """
        for entry in self.cities:
            if entry.get('name') not in self.cityInfo.keys():
                self.cityInfo.update({entry.get('name'):entry})

    def getCityList(self):
        """
        Returns list of cities.
        """
        return self.cityInfo.keys()

    def isAvailable(self, city):
        """
        Validates if the city is available in the dataset.
        Returns True if available else False.
        city - city being queried for.
        """
        if city in self.cityInfo.keys():
            return True
        return False
  
    def getCityDetails(self,city):
        """
        Returns details of the city if city exists in the dataset, 
        else returns None.
        city - city name for which details are queried for.
        """
        if city in self.cityInfo.keys():
            return self.cityInfo.get(city)
        return None


