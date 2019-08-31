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

class UserInterface(QMainWindow):
    ''' Main User Interface Window '''
    
    def __init__(self, media_collector):
        super().__init__()

        self.media_collector = media_collector
        self.setupUI()

    def setupUI(self):
        ''' Sets up and shows the GUI '''
        
        # setting up main window
        self.setObjectName("MainWindow")
        self.setWindowTitle("ABLE Test")
        self.resize(300, 300)
        self.setMinimumSize(200, 200)
        self.setWindowIcon(QIcon(self.media_collector.ableLogo()))
        self.setStyleSheet('''QMainWindow, QMessageBox, QLabel {background-color: #2a2a2a; color: white;}
                              QPushButton {background-color: #535353; color: white;}''')
        
        # setting up image button
        quit_button = QImageButton(QPixmap(self.media_collector.exitIcon()), 
                                   QPixmap(self.media_collector.hoverExitIcon()), 
                                   QPixmap(self.media_collector.pressedExitIcon()), self)
        
        quit_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        quit_button.setCursor(QCursor(Qt.PointingHandCursor))
        quit_button.clicked.connect(self.quitApp)

        # setting up layout
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        grid.addWidget(quit_button, 1, 1, Qt.AlignCenter)
        wid.setLayout(grid) 


        
    def closeEvent(self, event):
        ''' presents popup and checks dialog result when exiting application '''
        
        is_exit = self.showQuitPopup()
        if is_exit:
            event.accept()
        else:
            event.ignore()
    
    def quitApp(self):
        ''' presents popup and checks dialog result '''
        
        is_exit = self.showQuitPopup()
        if is_exit:
            sys.exit(0)
        else:
            pass

    
    def showQuitPopup(self):
        ''' shows quitting pop up '''
        
        exit_popup = QIconPopup("Demo popup message", "\nDo you want to close the app?", 
                               QPixmap(self.media_collector.exitIcon()), self)
        
        return exit_popup.exec() == 0
