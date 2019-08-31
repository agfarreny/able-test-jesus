'''
Module cointaining personalized widget classes for the GUI.

Classes
-------
QImageButton
    Interactive button class with a given icon QPixmap

QIconPopup
    Message Box class with a given icon QPixmap
'''

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMessageBox, QPushButton, QAbstractButton


class QImageButton(QAbstractButton):
    '''
    Prepares a QPixmap as a buton

    Methods
    -------
    paintEvent(event)
        Sets up the image of the button at each state
    sizeHint()
        Sets up button size.
    '''

    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
        """
        Parameters
        ----------
        pixmap : QPixmap
            pix map to set image of button's normal state 
        pixmap_hover : QPixmap
            pix map to set image of button's hover state 
        pixmap_pressed : QPixmap
            pix map to set image of button's pressed state 
        parent : optional
        """
        
        super(QImageButton, self).__init__(parent)
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        ''' Paints the specific icon for the related button status (normal, hover, pressed) ''' 
        chosen_btn_img = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            chosen_btn_img = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), chosen_btn_img)

    def enterEvent(self, event):
        self.update()

    def leaveEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(100, 100)

class QIconPopup(QMessageBox):
    '''
    Message Box class which allows icon personalization

    Methods
    -------
    setupButtons()
        Sets up buttons
    setButtonStyle(button, style)
        Sets up a specific button (button) with a style (style)
    '''
    
    def __init__(self, title, message, info_icon, parent=None):
        '''
        Parameters
        ----------
        title : str
            string to set the popup's title
        message : str
            string to set the popup's information messge
        info_icon : QPixmap
            pix map to set the information icon
        parent : optional
        '''
        
        super(QIconPopup, self).__init__(parent)
        
        self.setWindowTitle(title)
        self.setText(message)
        self.setIconPixmap(info_icon.scaled(QSize(45, 45), Qt.KeepAspectRatio))

        self.setupButtons()

       
    def setupButtons(self):
        ''' sets up buttons '''
        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")
        cancel_button = QPushButton("Cancel")
                
        self.addButton(yes_button, QMessageBox.YesRole )
        self.addButton(no_button, QMessageBox.NoRole)
        self.addButton(cancel_button, QMessageBox.RejectRole)

        self.setDefaultButton(cancel_button)
