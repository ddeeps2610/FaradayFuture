#!/usr/bin/env python

from Tkinter import *
from ttk import *


class View(object):
    """
    Class to define view of the UI
    """
    def __init__(self):
        """
        Initializes the view.
        """
        self.parent = Tk()
        self.parent.title("City Information")

        self.initialise_ui()
        self.controller = None

    def initialise_ui(self):
        """
        Initializes the view with basic elements.
        """
        # Define frames
        self.frame = Frame(self.parent)
        self.frame.pack()
        self.bottomFrame=Frame(self.parent)
        self.bottomFrame.pack(side=BOTTOM)
 
        # Define basic elements
        # Label to state select city 
        label = Label(self.frame, text='Select city: ')
        label.pack(side=LEFT)
        
        # Combobox to select cities. It is currently loaded with none.
        self.cityVar = StringVar()
        self.cityCombobox = Combobox(self.frame, textvariable=self.cityVar)
        self.cityCombobox['values']=['None']
        self.cityCombobox.current(0)
        self.cityCombobox.pack(side=LEFT)

        # Button to search details
        searchFunction = lambda : self.controller.loadDetails(
            self.cityVar.get())
        self.searchButton = Button(
            self.frame, 
            text="Search", 
            command=searchFunction)
        self.searchButton.pack(side=LEFT)

        
 
        self.closeButton = Button (self.frame, text = "Close", command = self.close_window)
        self.closeButton.pack(side=LEFT)
        
 
    def register(self, controller):
        """ 
        Register a controller to give callbacks to. 
        controller - Controller object to be registered for callback.
        """
        self.controller = controller


    def loadCityList(self, cityList):
        """
        Loads the combobox with list of cities.
        cityList - list of cities to be enlisted in combobox.
        """
        self.cityCombobox['values']=cityList
        self.cityCombobox.current(0)       
         

    def loadCityDetails(self, cityDetails):
        """
        Loads details of the cities when Search button is pressed.
        NOTE: Only required details about the city is displayed.
        cityDetails - city details dictionary object to be displayed.
        """
        # Clear the entries from previous search
        self.bottomFrame.destroy()
        self.bottomFrame=Frame(self.parent)
        self.bottomFrame.pack(side=BOTTOM)

        # Validate cityDetails
        if cityDetails == None:
            label = Label(self.bottomFrame, text='Details not available')
            label.pack() 
        
        # If city details are available, dispaly them. If any of the entry is 
        # not available, ignore the entry
        if cityDetails.get('county_name'):       
            self.countyText = Text(self.bottomFrame, height=1, width=50)
            self.countyText.insert(
                END, 'County: '+cityDetails.get('county_name'))
            self.countyText.configure(state='disabled')
            self.countyText.pack()

        if cityDetails.get('state_name'):
            self.stateText = Text(self.bottomFrame, height=1,width=50)
            self.stateText.insert(END,'State: '+cityDetails.get('state_name'))
            self.stateText.configure(state='disabled')
            self.stateText.pack()

        if cityDetails.get('url'):
            self.urlText = Text(self.bottomFrame, height=1,width=50)
            self.urlText.insert(END,'URL: '+cityDetails.get('url'))
            self.urlText.configure(state='disabled')
            self.urlText.pack()

        if cityDetails.get('description'):
            self.descrText = Text(self.bottomFrame, height=1,width=50)
            self.descrText.insert(
                END,'Description: '+cityDetails.get('description'))
            self.descrText.configure(state='disabled')
            self.descrText.pack()

        if cityDetails.get('primary_latitude'):
            self.latText = Text(self.bottomFrame, height=1,width=50)
            self.latText.insert(
                END, 'Latitude: '+cityDetails.get('primary_latitude'))
            self.latText.configure(state='disabled')
            self.latText.pack()

        if cityDetails.get('primary_longitude'):
            self.longText = Text(self.bottomFrame, height=1,width=50)
            self.longText.insert(
                END, 'Longitude: '+cityDetails.get('primary_longitude'))
            self.longText.configure(state='disabled')
            self.longText.pack()


    def close_window (self):
        """
        Closes the UI.
        """ 
        self.parent.destroy()        


    def main_loop(self):
        """
        Runs the UI for user interactions.
        """
        mainloop()

