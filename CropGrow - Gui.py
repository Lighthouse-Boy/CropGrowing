import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CropWindow(QMainWindow):
    """This is class creates a main window"""
    #constructor

    def __init__(self):
        super().__init__() # Call super class constructor
        self.setWindowTitle("Crop Simulator") # set window title

def main():
    crop_simulation = QApplication(sys.argv) # create new application
    crop_window = CropWindow() # create new instance of main window
    crop_window.show() #make instance visable
    crop_window.raise_() #top of window stack
    crop_simulation.exec() # monitor app

if 
