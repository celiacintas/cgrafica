from curva_bezier import curva_bezier, bernstein
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#bernstein = lambda i, n, t: comb(n, i) * ( t**(n-i) ) * (1 - t)**i

P1 = np.array([[1, 1, 0], [0.5, 0.5, 2.0], [1.5, 1.5, 4.0], [1, 1, 6.0]])
angles = [ [np.pi/2, np.pi, 3*np.pi/2, 0], [np.pi/2,np.pi, 3*np.pi/2, 0]]

def generate_sections(Pij, angles):
    points = []
    lines = []

    for a in angles:
        for i in range(Pij.shape[0]):
                points.append([Pij[i][0]*np.cos(a), Pij[i][1]*np.sin(a), Pij[i][2]])
        lines.append(points)
        points = []        
    return np.array(lines, dtype=np.float)

if __name__ == "__main__":
        totalsx = []
        totalsy = []
        totalsz = []
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for a in angles:
            Pij = generate_sections(P1, a)
            print Pij
            for i in range(Pij.shape[0]):
                xpoints = [p[0] for p in Pij[i]]
                ypoints = [p[1] for p in Pij[i]]
                zpoints = [p[2] for p in Pij[i]]
                print len(xpoints), Pij.shape
                xvalues, yvalues, zvalues = curva_bezier(Pij, xpoints, ypoints, zpoints)
                totalsx.append(xvalues)
                totalsy.append(yvalues)
                totalsz.append(zvalues)
                #ax.scatter(xpoints, ypoints, zpoints) #, zs=0, zdir='z', label='zs=0, zdir=z')
                ax.plot(xpoints, ypoints, zpoints, 'ro-')
        ax.plot_surface(totalsx, totalsy, totalsz, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
        ax.plot_wireframe(totalsx, totalsy, totalsz)
        
        plt.show()