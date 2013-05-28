import math
import time
import random
import numpy
import scipy
from curva_bezier import curva_bezier, bernstein
from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

bernstein = lambda i, n, t: comb(n, i) * ( t**(n-i) ) * (1 - t)**i

Pij = np.array([[[-1.5, -1.5, 4.0], [-0.5, -1.5, 2.0],[0.5, -1.5, -1.0], [1.5, -1.5, 2.0]],
    [[-1.5, -0.5, 1.0], [-0.5, -0.5, 3.0], [0.5, -0.5, 0.0], [1.5, -0.5, -1.0]],
    [[-1.5, 0.5, 4.0], [-0.5, 0.5, 0.0], [0.5, 0.5, 3.0], [1.5, 0.5, 4.0]],
    [[-1.5, 1.5, -2.0], [-0.5, 1.5, -2.0], [0.5, 1.5, 0.0], [1.5, 1.5, -1.0]]])

if __name__ == "__main__":
        totalsx = []
        totalsy = []
        totalsz = []
    
        for i in range(Pij.shape[0]):

            xpoints = [p[0] for p in Pij[i]]
            ypoints = [p[1] for p in Pij[i]]
            zpoints = [p[2] for p in Pij[i]]
            
            xvalues, yvalues, zvalues = curva_bezier(Pij, xpoints, ypoints, zpoints)
            totalsx.append(xvalues)
            totalsy.append(yvalues)
            totalsz.append(zvalues)
            
            #X = Y = np.arange(-5, 5, 0.25)
            #ylen = len(Y)
            #X, Y = np.meshgrid(p[0], p[1]
            #R = np.sqrt(X**2 + Y**2)
            #Z = np.sin(R)
            #Z = zpoints
            print p
            #plt.plot(xvals, yvals)
            #    plt.plot(xpoints, ypoints, "b*", markersize=10)
            #for nr in range(len(control_points)):
            #        plt.text([nr][0], control_points[nr][1], " " + str(nr))
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(xpoints, ypoints, zpoints) #, zs=0, zdir='z', label='zs=0, zdir=z')
        ax.plot_wireframe(totalsx, totalsy, totalsz)
        plt.show()



"""def P(U,V):

    m = n = 4
 
    
    t = np.linspace(0.0, 1.0, 100)
    polyBm = np.array([ bernstein(i, m-1, t) for i in range(0, m)])
    polyBn = np.array([ bernstein(i, n-1, t) for i in range(0, n)])
    
    p = []
    for i in range(m):
        sumx = sumy = sumz = 0
        px = []
        py = []
        pz = []
        for j in range(n):
            sumx += polyBm[i]*polyBn[j]* Pij[i][j][0]
            sumy += polyBm[i]*polyBn[j]* Pij[i][j][1]
            sumz += polyBm[i]*polyBn[j]* Pij[i][j][2]
            px.append(sumx)
            py.append(sumy)
            pz.append(sumz)
        p.append(sum(px))
        p.append(sum(py))
        p.append(sum(pz))
    return Pij, p
"""