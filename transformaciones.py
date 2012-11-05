#! /usrbin/python2
# -*- coding: utf-8 -*-

#Computacion Grafica - Delrieux - Cap 3  

import sys, random
from PyQt4 import QtGui, QtCore
from numpy import arange, pi, sin, cos

class Transformaciones(QtGui.QWidget):
	    
	    def __init__(self):
		    super(Transformaciones , self).__init__()
		    self.initUI()
		    self.miPix = QtGui.QPixmap("imagenes/gnu.png")

	    def initUI(self):
		    self.setGeometry(0, 0, 500, 500)
		    self.setWindowTitle('Transformaciones')
		    self.show()

	    def paintEvent(self, e):
		    qp = QtGui.QPainter()
		    qp.begin(self)
		    qp.drawPixmap(50, 50, self.miPix)
		    #self.rotate(qp, grados=35)
		    self.scaled(qp)
		    #self.traslate(qp)
		    qp.drawPixmap(50, 50, self.miPix)
		    qp.end()

            def rotate(self, qp, grados):
		   alpha = pi / 180 * grados
		   qp.setTransform(QtGui.QTransform(QtGui.QMatrix(cos(alpha), sin(alpha), -sin(alpha), cos(alpha), 0, 0))) 

	    def traslate(self, qp):
		   qp.setTransform(QtGui.QTransform(QtGui.QMatrix(1, 0, 0, 1, 30, 30))) 

	    def scaled(self, qp):
		   qp.setTransform(QtGui.QTransform(QtGui.QMatrix(0.2, 0, 0, 1.0, 0, 0))) 

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Transformaciones()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
