'''
Main module from where the application is started.

Controlls the modules and view of the application.

Classes
-------
App
    Contains the main method
'''

import sys
from UserInterface import UserInterface
from Modules import MediaCollector
from PyQt5.QtWidgets import QApplication

class App():
	def main(self):
		app = QApplication(sys.argv)
		mc = MediaCollector()
		ui = UserInterface(mc)
		ui.show()
		sys.exit(app.exec_())

if __name__ == "__main__":
	App().main()
