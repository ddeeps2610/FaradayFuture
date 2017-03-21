This file defines how to use the class. The help menu for launch class is 
mentioned below.


###############################################################################
Help Menu:
usage: launchUI.py [-h] [--datafile DATAFILE]

Launches UI for displaying city information

optional arguments:
  -h, --help           show this help message and exit
  --datafile DATAFILE  [Optional] Data file that contains the city
                       information. Default value for the datafile name is
                       'ca.json'.
###############################################################################

Example:
1. To enlist the help options.
python launchUI.py -h


2. To launch the UI with default file ca.json
python launchUI.py


3. To launch the UI with other data file
python launchUI.py --datafile='<otherDataFile>'

###############################################################################
UI Operations:
Step1: Select the city from the combobox.
Step2: Click on Search button to load the details.
Step3: Go back to Step1 for other searches.
Step4: Click on Close button to close the appliction.
