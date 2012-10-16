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
		    self.fillPoly(qp, aristas)
		    qp.end()

	    def drawPoly(self, qp, aristas):
		    	qp.drawLine(aristas[0][0], aristas[0][1], aristas[1][0], aristas[1][1])
		    	qp.drawLine(aristas[1][0], aristas[1][1], aristas[2][0], aristas[2][1])
		    	qp.drawLine(aristas[2][0], aristas[2][1], aristas[0][0], aristas[0][1])

	    def fillPoly(self, qp, aristas):
		    size = self.size()
		    qp.setPen(QtCore.Qt.green)
		    print size
		    for y in range(size.height()):
			    for x in range(size.width()):
			    	if self.pointInPoly(x, y, aristas):
				    qp.drawPoint(x,y)
				    print "dibuje en %d ,%d:" %(x, y)

	    def pointInPoly(self, x, y, aristas):
		    #  http://bytes.com/topic/c/answers/941695-point-polygon
		   n = len(aristas)
		   inside = False

		   p1x,p1y = aristas[0]
                   for i in range(n+1):
                         p2x,p2y = aristas[i % n]
                         if (y > min(p1y,p2y)) & (y <= max(p1y,p2y)) & (x <= max(p1x,p2x)):
                                 if p1y != p2y:
				           xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                                 if p1x == p2x or x <= xinters:
                                           inside = not inside
                         p1x,p1y = p2x,p2y
		   return inside


def main():
    app = QtGui.QApplication(sys.argv)
    ex = PoligonosPaint()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
