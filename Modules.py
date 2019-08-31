'''
User Interface Module contains the UI class for the app

Classes
-------
UserInterface
    Main User Interface Window
'''

import os, sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import (QWidget, QApplication, QSizePolicy, 
                             QGridLayout, QMessageBox, QPushButton, 
                             QAbstractButton, QMainWindow)

from PersonalizedWidgets import QImageButton, QIconPopup

class MediaCollector():
    ''' Class to manage media files '''
    def __init__(self):
    	# obtaining media location path (path relative to OS)
        self.MEDIA_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "media" + os.path.sep

    def ableLogo(self):
    	''' Returns ABLE logo '''
    	return self.MEDIA_PATH + "able_logo.png"

    def exitIcon(self):
    	''' Returns Exit icon '''
    	return self.MEDIA_PATH + "exit.png"

    def hoverExitIcon(self):
    	''' Returns Exit icon when hover '''
    	return self.MEDIA_PATH + "exit_hover.png"    	

    def pressedExitIcon(self):
    	''' Returns Exit icon when pressed '''
    	return self.MEDIA_PATH + "exit_pressed.png"    	
