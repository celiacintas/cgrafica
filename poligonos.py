#! /usrbin/python2
# -*- coding: utf-8 -*-

#pseudo cod tomado del apunte de 
#Computacion Grafica - Delrieux - Cap 2  

import sys, random
from PyQt4 import QtGui, QtCore

import sys, random
from PyQt4 import QtGui, QtCore
from numpy import arange

class PoligonosPaint(QtGui.QWidget):
	    
	    def __init__(self):
		super(PoligonosPaint , self).__init__()
		self.initUI()

	    def initUI(self):
		    self.setGeometry(0, 0, 500, 500)
		    self.setWindowTitle('Poligonos')
		    self.show()

	    def paintEvent(self, e):
		    qp = QtGui.QPainter()
		    qp.begin(self)
		    aristas = [(100, 100), (200, 200), (50, 100) ]
		    self.drawPoly(qp, aristas)
		    qp.end()

	    def drawPoly(self, qp, aristas):
		    	qp.drawLine(aristas[0][0], aristas[0][1], aristas[1][0], aristas[1][1])
		    	qp.drawLine(aristas[1][0], aristas[1][1], aristas[2][0], aristas[2][1])
		    	qp.drawLine(aristas[2][0], aristas[2][1], aristas[0][0], aristas[0][1])

	    def fillPoly(self, qp, aristas):
		    pass

	    def pointInPoly(self, px, py, aristas):
		    pass

def main():
    app = QtGui.QApplication(sys.argv)
    ex = PoligonosPaint()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
