# importing libraries
from importlib.resources import path
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import  os

from keras.preprocessing.image import img_to_array
import tensorflow as tf
from keras.models import load_model
import numpy as np
import cv2
from keras.preprocessing import image
import tkinter as tk
from tkinter import *


from gtts import gTTS
from playsound import  playsound

# window class
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint")

        self.setGeometry(100, 100, 800, 600)

        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.black)

        # variables
        # drawing flag
        self.drawing = False

        self.brushSize = 40

        self.brushColor = Qt.white

        # QPoint object to tract the point
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")

        exitMenu = mainMenu.addMenu("Close")
        #creating a exit action
        exitAction = QAction("Exit",self)
        exitMenu.addAction(exitAction)
        exitAction.triggered.connect(self.close)

        # creating save action
        saveAction = QAction("Save and Predict", self)
        # adding save to the file menu
        fileMenu.addAction(saveAction)
        # adding action to the save
        saveAction.triggered.connect(self.save)

        # creating clear action
        clearAction = QAction("Clear", self)
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(self.clear)

        

    # method for checking mouse cicks
    def mousePressEvent(self, event):

        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            # make drawing flag true
            self.drawing = True
            # make last point to the point of cursor
            self.lastPoint = event.pos()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):

        if (event.buttons() & Qt.LeftButton) & self.drawing:
            # creating painter object
            painter = QPainter(self.image)

            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False

    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)

        # draw rectangle on the canvas
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _  = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        self.image.save(filePath)
        labels = [u'\u091E', u'\u091F', u'\u0920', u'\u0921',u'\u0922',u'\u0923',u'\u0924',u'\u0925',u'\u0926',u'\u0927',u'\u0915',u'\u0928',u'\u092A',u'\u092B',u'\u092c',u'\u092d',u'\u092e',u'\u092f',u'\u0930',u'\u0932',u'\u0935',u'\u0916',u'\u0936',u'\u0937',u'\u0938',u'\u0939','?????????','?????????','?????????',u'\u0917',u'\u0918',u'\u0919',u'\u091a',u'\u091b',u'\u091c',u'\u091d',u'\u0966',u'\u0967',u'\u0968',u'\u0969',u'\u096a',u'\u096b',u'\u096c',u'\u096d',u'\u096e',u'\u096f']
        print("[INFO] loading network...")
        #filename = os.environ.get('LAST_PATH')
        test_image = cv2.imread(filePath)
        image = cv2.resize(test_image, (32, 32))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = np.expand_dims(image, axis=0)
        image = np.expand_dims(image, axis=3)
        model = tf.keras.models.load_model("C:/Users/banda/PycharmProjects/Hindi-OCR-master/HindiModel3.h5")
        lists = model.predict(image)[0]
        print("The letter is ", labels[np.argmax(lists)]," ")


        #w = QWidget()
        b = QMessageBox()
        #QString text = QString("The letter is: ").arg(labels[np.argmax(lists)])
        b.setText(labels[np.argmax(lists)])

        mytext= labels[np.argmax(lists)]
        
        if mytext == '???':
            playsound("C:\Sounds\ka.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\kha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ga.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\gha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\nga.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\cha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\chha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ja.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\jha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\nya.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ta.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ttha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\da.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ddha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ana.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\tha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\thha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\dha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\dhha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\na.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\pa.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\pha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ba.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\bha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ma.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ya.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ra.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\la.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\va.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\sha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\shha.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\sa.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\ha.mp3")
        elif mytext == 'ksha':
            playsound("C:\Sounds\ksha.mp3")
        elif mytext == 'thra' or mytext == '?????????':
            playsound("C:\Sounds\thra.mp3")
        elif mytext == 'gya':
            playsound("C:\Sounds\gya.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\one.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\two.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\three.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\four.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\five.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\six.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\seven.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\eight.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\nine.mp3")
        elif mytext == '???':
            playsound("C:\Sounds\zero.mp3")

        self.close()

    # method for clearing every thing on canvas
    def clear(self):
        self.image.fill(Qt.black)
        self.update()
    
# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())