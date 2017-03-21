#!/usr/bin/env python


import os
from model import Model
from controller import Controller
from view import View
import argparse

if (__name__ == "__main__"):
    """
    Launches the UI, loads the dataset and handles user inputs.
    """
    parser = argparse.ArgumentParser(
        description='Launches UI for displaying city information')
    parser.add_argument('--datafile', default='ca.json',
        help="""[Optional] Data file that contains the city information.
             Default value for the datafile name is 'ca.json'.
             """)
    args = parser.parse_args()

    if os.path.exists(args.datafile) and os.path.isfile(args.datafile):
        view = View()
        model = Model(args.datafile)
        controller = Controller(model, view)

        view.main_loop()
    else:
        print "Datafile does not exist or is not a file"

