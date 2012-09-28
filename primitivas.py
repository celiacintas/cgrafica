#! /usrbin/python2
# -*- coding: utf-8 -*-

#pseudo cod tomado del apunte de 
#Computacion Grafica - Delrieux - Cap 2  

import sys, random
from PyQt4 import QtGui, QtCore

import sys, random
from PyQt4 import QtGui, QtCore
from numpy import arange

class PrimitivePaint(QtGui.QWidget):
	    
	    def __init__(self):
		super(PrimitivePaint , self).__init__()
		self.initUI()

	    def initUI(self):
		    self.setGeometry(300, 300, 400, 300)
		    self.setWindowTitle('Primitivas')
		    self.show()

	    def paintEvent(self, e):
		    qp = QtGui.QPainter()
		    qp.begin(self)
		    self.drawPoints(qp)
		    self.drawLineDDA(qp, 100.0, 300.0, 30.0, 60.0)
		    self.drawLineBresenham(qp, 100, 200, 30, 50)
		    self.drawCircleDDA(qp, 100.0)
		    self.drawCircleBresnham(qp, 80.0)
		    qp.end()
	    
	    def drawPoints(self, qp):
		    qp.setPen(QtCore.Qt.green)
		    size = self.size()
		    for i in range(10):
			    x = random.randint(1, size.width()-1)
			    y = random.randint(1, size.height()-1)
			    qp.drawPoint(x, y)     

	    def drawLineDDA(self, qp, x0, x1, y0, y1):
		    qp.setPen(QtCore.Qt.blue)
		    m = (y1 - y0)/(x1 - x0)
		    y = y0
		    for x in arange(x0, x1, 0.1):
			    qp.drawPoint(x, y)
			    print "x: ",x 
			    print "y: ",y 
			    y += m

            def drawLineBresenham(self, qp, x0, x1, y0, y1):
		    qp.setPen(QtCore.Qt.yellow)
		    dx = x1 - x0; dy = y1 - y0
		    ix = 2*dx; iy = 2*dy
		    y = y0 ; e = iy - dx

		    for x in range(x0, x1):
			    print "x: ",x 
			    print "y: ",y 
			    qp.drawPoint(x, y)
			    if e > 0:
				    y += 1
				    e -= ix
			    e += iy	

	    def drawCircleDDA(self, qp, radio):
		    qp.setPen(QtCore.Qt.red)
		    
		    rx = radio
		    x = round(rx); y = 0

		    while (y < x):
			    qp.drawPoint(x, y) 
			    qp.drawPoint(y, x)
			    qp.drawPoint(-x, y) 
			    qp.drawPoint(-y, x)
			    qp.drawPoint(x, -y) 
			    qp.drawPoint(y, -x)
			    qp.drawPoint(-x,-y) 
			    qp.drawPoint(-y,-x)
			    rx -= y/rx
			    x = round(rx)
			    y+= 1

	    def drawCircleBresnham(self, qp, radio): 
		    qp.setPen(QtCore.Qt.magenta)

		    x = radio; y = 0
		    e = 0

		    while (y < x):
			    qp.drawPoint(x, y) 
			    qp.drawPoint(y, x)
			    qp.drawPoint(-x, y) 
			    qp.drawPoint(-y, x)
			    qp.drawPoint(x, -y) 
			    qp.drawPoint(y, -x)
			    qp.drawPoint(-x,-y) 
			    qp.drawPoint(-y,-x)
			    e += 2*y +1
			    y += 1
			    if (2*e) > (2*x - 1):
				    x -= 1
				    e -= 2*x + 1
	
def main():
    app = QtGui.QApplication(sys.argv)
    ex = PrimitivePaint()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
