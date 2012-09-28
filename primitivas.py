#! /usrbin/python2
# -*- coding: utf-8 -*-

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
		    self.setGeometry(300, 300, 280, 170)
		    self.setWindowTitle('Primitivas')
		    self.show()

	    def paintEvent(self, e):
		    qp = QtGui.QPainter()
		    qp.begin(self)
		    self.drawPoints(qp)
		    self.drawLineDDA(qp, 100.0, 300.0, 30.0, 60.0)
		    self.drawLineBresenham(qp, 100, 200, 30, 50)
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

def main():
    app = QtGui.QApplication(sys.argv)
    ex = PrimitivePaint()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
