#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from numpy import random
import numpy as np
from curva_bspline import Bspline
from pyglet.gl import *
import pyglet 

class BSplineSurface():
    def __init__(self, m):
        self.m = m
        self.points = self.generateVase()
        self.knots1 = self.getKnots(self.points.shape[0])
        self.knots2 = self.getKnots(self.points.shape[1])

    def getKnots(self, lenPoints):
        knots = []
        numKnots = lenPoints + 4
        innerKnots = numKnots - 8

        for i in range(4):
            if i < numKnots/2:
                knots.append(0)
            else:
                break

        if innerKnots < 0 and numKnots%2 != 0:
            innerKnots = 1

        for i in range(innerKnots):
            knots.append(i/innerKnots+1.0)
  
        for i in range(4):
            if i < numKnots/2:
                knots.append(1)
            else:
                break

        return knots

    def basisFunction(self, u, i, knots, k=3):
        if k == 1:
            if ((knots[i] < knots[i+1] and knots[i] <= u and u < knots[i+1]) or (u == 1 and knots[i+1] == 1)):
                result = 1
            else:
                result = 0
        else:
            knotDelta = knots[i+k-1] - knots[i]
            knotDelta1 = knots[i+k]   - knots[i+1]

            if(knotDelta != 0):
                r1 = ((u-knots[i]) / knotDelta) * self.basisFunction(u, i, knots, k-1)
            else:
                r1 = 0
            
            if(knotDelta1 != 0):
                r2 = ((knots[i+k] - u) / knotDelta1) * self.basisFunction(u, i+1, knots, k-1)
            else:
                r2 = 0
            
            result = r1 + r2

        return result

    def generateControlPoints(self):
        """generate the form  of the example in 
        http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/surface/bspline-construct.html"""

        control_points = []
        w = h = 4
        cw = (w - 1)/2.0
        ch = (h - 1)/2.0

        for x in range(w):
            fila = []
            for z in range(h):
                fila.append([10*(x-cw), -((x-cw)*(x-cw)+(z-ch)*(z-ch))*2, 10*(z-ch)])
            control_points.append(fila)

        control_points = np.array(control_points)
        control_points = control_points.reshape((4, 4, 3))
        return control_points    
    
    def generateVase(self):
        return np.array([[[2, 1.2, 0.5],[1, 1.2, 0.5],[1, 2, 0.5],[2,2,0.5]],
                         [[1.75, 1.5, 1.5],[1.45, 1.5, 1.5],[1.45, 1.75, 1.5],[1.75,1.75,1.5]],
                         [[2, 1.2, 2.5],[1, 1.2, 2.5],[1, 2, 2.5],[2,2,2.5]],
                         [[1.75, 1.5, 3.5],[1.45, 1.5, 3.5],[1.45, 1.75, 3.5],[1.75,1.75,3.5]]])

def getpoints(points):
    xpoints = []
    ypoints = []
    zpoints = []
    for row in points:
            xpoints = xpoints + [p[0] for p in row]
            ypoints = ypoints + [p[1] for p in row]
            zpoints = zpoints + [p[2] for p in row]

    return xpoints, ypoints, zpoints



if __name__ == '__main__':
    bsplineSur = BSplineSurface(3)
    
    N = 160
    delta = 1.0/N
    us = np.linspace(0, 1, N)
    vs = np.linspace(0, 1, N)
    done_points = []
    for u in us:
        fila = []
        for v in vs:
            vertex = np.array([0.0, 0.0, 0.0], dtype=np.float)
            for i in range(bsplineSur.points.shape[0]):
                for j in range(bsplineSur.points.shape[1]):
                    b1 = bsplineSur.basisFunction(u, i, bsplineSur.knots1, 4)
                    b2 = bsplineSur.basisFunction(v, j, bsplineSur.knots2, 4)
                    vertex = vertex + bsplineSur.points[i][j] * (b1 * b2)
            fila.append(vertex)
        done_points.append(fila)
    
    points = np.array(done_points)
   
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    xpoints, ypoints, zpoints = getpoints(bsplineSur.points)
    ax.plot(xpoints, ypoints, zpoints, 'ro') 
    coll = ax.add_collection3d(Poly3DCollection(done_points))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


