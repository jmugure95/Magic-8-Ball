'''
    Import the packages needed to write the program

'''

import sys
import random
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

'''
    Create a class that will contain all the methods 
    performing various functions in the program window


    Here we create a new class called Example. The Example class inherits from the QMainWindow class. 
    This means that we call two constructors: the first one for the Example class and the second one for the inherited class. 
    The __init__() method is a constructor method in Python language.

'''

class Example(QMainWindow): 

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 600))         # Set the window size
        self.setWindowTitle("Magic 8 ball Game")     # Set the window name 

        
        self.questionLabel = QLabel(self)            # PyQt5 uses QLabel for displaying text or an image 
        self.questionLabel.setText('Enter Your Question:') # Set the games question
        self.line = QLineEdit(self)                   # QLineEdit provides an input field(box) in which one line of text can be entered

        self.line.move(200, 20)    # These four lines of code help position and move the label and the input field
        self.line.resize(200, 32)
        self.questionLabel.move(40, 20)
        self.questionLabel.adjustSize()  #adjustsize() is a method used to auto adjust the size of the label according to the text


        button = QPushButton('OK', self)  # QPushButton is used to create the button widget in the GUI
        button.clicked.connect(self.magicMethod) # Tells the program that when this button is clicked, search for the function called and perform the action in that function 
        button.resize(200,32) # method used to resize the button
        button.move(200, 60)  #method used to move(position) the button

        

        button2 = QPushButton('Play Again', self)      
        button2.clicked.connect(self.askMethod)
        button2.resize(200,32)              # The resize() method resizes the widget. It is 200px wide and 32px high.
        button2.move(200, 120)              # The move() method moves the widget to a position on the screen at x=200, y=120 coordinates.

        button3 = QPushButton('Clear',self)
        button3.clicked.connect(self.clearMethod)
        button3.resize(200,32)
        button3.move(200, 190)

        button4 = QPushButton('Quit',self)
        button4.clicked.connect(self.quitMethod)
        button4.resize(200,32)
        button4.move(200, 220)
  

    '''
        Create the functions that will be called upon when particular buttons are clicked

    '''

    def askMethod(self):     # the function when called will print 'Thinkiing' and sleep for 3 seconds and return a random response from the responses list
    	print("Thinking...")
    	time.sleep(3)
    	responses = ["You win","Probably Yes","Probably Not","Try Again","Open the box","Be careful","You are a champion","Hang In There","Patience Pays","You are Excellent","We see you"]
    	print(random.choice(responses))


    def clearMethod(self):  #The function when called, will clear any entered in the widget by the user, PyQt5 makes use of the clear() method
    	self.line.clear()   

    def quitMethod(self):  # The function closes the GUI window when the user clicks the QUIT button
    	sys.exit()


'''
    (Simple English)
    Think of the next part as the superstar of our program.
    Without it, we have no program at all to run 


    It is the mainloop of the application. Event handling starts from this point. 
    It receives events from the window system and dispatches them to the application widgets.
    It ends if we call the exit() method or the main widget is destroyed. 
    
'''
   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)   #QApplication is used to create an application object
    mainWin = Example()    
    mainWin.show()              # The show() method displays the widget on the screen. A widget is first created in memory and later shown on the screen.
    sys.exit( app.exec_())      # sys.exit() method ensures a clean exit.






























































    

# from PyQt5 import QtCore, QtGui, QtWidgets 
# import sys 
  
# class Ui_MainWindow(object): 
  
#     def setupUi(self, MainWindow): 
#         MainWindow.resize(506, 312) 
#         self.centralwidget = QtWidgets.QWidget(MainWindow) 
          
#         # adding pushbutton 
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget) 
#         self.pushButton.setGeometry(QtCore.QRect(200, 150, 93, 28)) 
  
#         # adding signal and slot  
#         self.pushButton.clicked.connect(self.changelabeltext) 
    
#         self.label = QtWidgets.QLabel(self.centralwidget) 
#         self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))       
  
#         # keeping the text of label empty before button get clicked 
#         self.label.setText("")      
         
#         MainWindow.setCentralWidget(self.centralwidget) 
#         self.retranslateUi(MainWindow) 
#         QtCore.QMetaObject.connectSlotsByName(MainWindow) 
  
#     def retranslateUi(self, MainWindow): 
#         _translate = QtCore.QCoreApplication.translate 
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) 
#         self.pushButton.setText(_translate("MainWindow", "Push Button")) 
          
#     def changelabeltext(self): 
  
#         # changing the text of label after button get clicked 
#         self.label.setText("You clicked PushButton")     
  
#         # Hiding pushbutton from the main window 
#         # after button get clicked.  
#         self.pushButton.hide()    
  
# if __name__ == "__main__":  
#     app = QtWidgets.QApplication(sys.argv)  
    
#     MainWindow = QtWidgets.QMainWindow()  
#     ui = Ui_MainWindow()  
#     ui.setupUi(MainW