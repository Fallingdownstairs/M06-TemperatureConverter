# -*- coding: utf-8 -*-
#Author:  Nathaniel Kickbush
#Date written: 07/17/23
#Assignment:   M06 Programming Assignment
#Short Desc:   Convert temperature to Celcius or fahrenheight with GUI

import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDoubleSpinBox, QLabel

from temperatureConverter import Ui_MainWindow

from convertedTemperatureDialogBox import Ui_convertedTemperatureDialog

class TempDialog(QDialog, Ui_convertedTemperatureDialog):
    
    def __init__(self, *args, obj=None, **kwargs):
        
        super(TempDialog, self).__init__(*args,**kwargs)
        
        self.setupUi(self)
        

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, obj=None, **kwargs):
        
        super(Window, self).__init__(*args,**kwargs)
        
        self.setupUi(self)

        self.celciusButton.clicked.connect(self.celciusClicked)
        
        self.fahrenheightButton.clicked.connect(self.fahrenheightClicked)
        
        self.converted = 0.00
        
    def openDialog(self):
        
        dialog = TempDialog(self)
        
        dialog.convertedTemperature.setText(f'{self.converted:.1f}')
        
        dialog.exec()
        
        
        
    def celciusClicked(self):
        
        self.converted = (float(self.temperatureSetting.text()) - 32) / 1.8
        
        self.openDialog()

        
    def fahrenheightClicked(self):
       
       self.converted = (float(self.temperatureSetting.text()) * 1.8) + 32 
       
       self.openDialog()
            
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()

print(window.temperatureSetting)
