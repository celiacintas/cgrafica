from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from numpy import random
import numpy as np
from curva_bspline import Bspline

class BSplineSurface():
    def __init__(self, points, m):
        self.m = m
        self.points = points
        self.knots1 = self.getKnots(points.shape[0])
        self.knots2 = self.getKnots(points.shape[1])

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
    #control_points = np.array([[[1, 1, 0], [2, 1, 0],[3, 1, 0], [4, 1, 0]],
    #[[1, 2, 0], [1, 3, 0],[1, 4, 0], [1, 5, 0]],
    #[[1, 5, 0], [2, 5, 0],[3, 5, 0], [4, 5, 0]],
    #[[4, 1, 0], [3, 3, -1],[4, 3, 0], [4, 4, 4]]])
    control_points = np.random.uniform(1, 2, size=16*3)
    
    control_points = control_points.reshape((4, 4, 3))
    bsplineSur = BSplineSurface(control_points, 3)
    done_points = []
    N = 40
    delta = 1.0/N
    us = np.linspace(0, 1, N)
    vs = np.linspace(0, 1, N)


    for u in us:
        fila = []
        for v in vs:
            vertex = np.array([0.0, 0.0, 0.0], dtype=np.float)
            for i in range(control_points.shape[0]):
                for j in range(control_points.shape[1]):
                    b1 = bsplineSur.basisFunction(u, i, bsplineSur.knots1, 2)
                    b2 = bsplineSur.basisFunction(v, j, bsplineSur.knots2, 3)
                    vertex = vertex + control_points[i][j] * (b1 * b2)
            fila.append(vertex)
        done_points.append(fila)
    

    done = np.array(done_points)
    print done.shape


    fig = plt.figure()
    ax = fig.gca(projection='3d')
    xpoints, ypoints, zpoints = getpoints(bsplineSur.points)
    ax.plot(xpoints, ypoints, zpoints, 'ro') #, zs=0, zdir='z', label='zs=0, zdir=z')
    #totalsx, totalsy, totalsz = getpoints(done_points)
    #verts = [zip(totalsx, totalsy, totalsz)]
    coll = ax.add_collection3d(Poly3DCollection(done_points))

    #ax.plot_wireframe(totalsx, totalsy, totalsz, cmap=coolwarm) #color='red')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
