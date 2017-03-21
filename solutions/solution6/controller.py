#!/usr/bin/env python

class Controller(object):
    """
    Class that controls the UI flow.
    """
    def __init__(self, model, view):
        """
        Initializes the controller and registers model and views.
        model - model that contains the dataset for the UI.
        view - view that defines the UI.
        """
        self.model = model
        self.view = view

        self.view.register(self)
        self.loadCityList()

    def loadCityList(self):
        """
        Calls UI to load the city list in the combobox during initialization.
        """
        cityList = self.model.getCityList()
        self.view.loadCityList(cityList)

    def loadDetails(self, city):
        """
        Calls the view to load the city details. City details are 
        obtained from the model. If the city is not present, the details
        will be None. The view will have to handle if the city details 
        does not exits.
        """
        self.view.loadCityDetails(self.model.getCityDetails(city))
