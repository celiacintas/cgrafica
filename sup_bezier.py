from curva_bezier import curva_bezier, bernstein
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

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
            print len(xpoints), Pij.shape
            xvalues, yvalues, zvalues = curva_bezier(Pij, xpoints, ypoints, zpoints)
            totalsx.append(xvalues)
            totalsy.append(yvalues)
            totalsz.append(zvalues)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(xpoints, ypoints, zpoints) #, zs=0, zdir='z', label='zs=0, zdir=z')
        ax.plot_surface(totalsx, totalsy, totalsz, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
        ax.plot_wireframe(totalsx, totalsy, totalsz)
        
        plt.show()