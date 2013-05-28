import argparse
import numpy as np
from scipy.misc import comb
from matplotlib import pyplot as plt

bernstein = lambda i, n, t: comb(n, i) * ( t**(n-i) ) * (1 - t)**i

def curva_bezier(control_points, xPoints, yPoints, zPoints=None, n=60):

    nPoints = control_points.shape[0]
    
    t = np.linspace(0.0, 1.0, n)

    poly = np.array([ bernstein(i, nPoints-1, t) for i in range(0, nPoints)])

    xvals = np.dot(xPoints, poly)
    yvals = np.dot(yPoints, poly)
    if zPoints:
        zvals = np.dot(zPoints, poly)
        return xvals, yvals, zvals
    else:
        return xvals, yvals


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description=
                                     'generate bezier curve with n control points in random positions')
    parser.add_argument("-nc", dest="ncurves", help='This option is used to set the number of curves')
    args = parser.parse_args()
    if not (args.ncurves):
        nc = 1
    else:
        nc = int(args.ncurves)
    for c in range(nc):
        n = 4    
        control_points = np.random.rand(n, 2)*100
        xpoints = [p[0] for p in control_points]
        ypoints = [p[1] for p in control_points]

        xvals, yvals = curva_bezier(control_points, xpoints, ypoints, n=1000)
        plt.plot(xvals, yvals)
        plt.plot(xpoints, ypoints, "b*", markersize=10)
        for nr in range(len(control_points)):
            plt.text(control_points[nr][0], control_points[nr][1], " " + str(nr))
    plt.show()