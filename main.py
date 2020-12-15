# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtCore import *
from PySide2 import QtGui
from PySide2.QtWidgets import *
from form import Ui_gui
from tensorflow import keras
from PIL import Image, ImageDraw
import numpy
import io


class gui(QWidget):
    def __init__(self):
        super(gui, self).__init__()
        self.gui = Ui_gui()
        self.gui.setupUi(self)
        self.net = keras.models.load_model("neuralnet\model")


    @Slot()
    def load(self):
        self.path = QFileDialog.getOpenFileName(self, "Load Image", "~/Desktop/",  "*.jpg *.png")
        self.path = self.path[0]
        print(self.path)
        self.pixmap = QtGui.QPixmap(self.path)
        self.gui.setpixmap(self.pixmap)


    @Slot()
    def recognize(self):

        pilimg = Image.open(self.path)
        pilimg = pilimg.convert('L')
        pilimg = numpy.array(pilimg)
        pilimg = pilimg.reshape(-1, 28, 28, 1)
        pilimg = pilimg.astype('float32')
        pilimg = pilimg / 255.0

        predict = self.net.predict(pilimg)
        print(predict)
        numer = numpy.argmax(predict)
        print(numer)

        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter = alpha[numer-1]
        self.gui.setletter(letter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = gui()
    widget.show()
    sys.exit(app.exec_())
