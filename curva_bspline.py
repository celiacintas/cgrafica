from __future__ import division

import matplotlib.pyplot as plt
from numpy import random


class Bspline():
    def __init__(self, points, m):
        self.M = len(points) - 1
        self.n = self.M - m + 1
        self.m = m
        self.points = points
        self.knots = [0] * self.m + [k / self.n for k in xrange(self.n + 1)] + [1] * self.m

    def curve(self, t):
        if t == 1:
            return self.points[-1]
        k = self.m
        while k + 1 < len(self.knots) and t > self.knots[k + 1]: 
            k += 1
        Nk = [1] + [0] * self.m
        V = lambda m, i, t: (t - self.knots[i]) / (self.knots[i + m] - self.knots[i]) \
                            if self.knots[i] != self.knots[i + m] \
                            else 0
        for i in xrange(1, self.m + 1):
            for j in xrange(i, -1, -1):
                if j:
                    Nk[j] = Nk[j] * V(i, k - j, t) + Nk[j - 1] * (1 - V(i, k - j + 1, t))
                else:
                    Nk[j] = Nk[j] * V(i, k - j, t)
        Nk.reverse()

        return [sum(p[j] * N for p, N in zip(self.points[k-self.m:k+1], Nk)) for j in (0, 1)]



if __name__ == '__main__':

    control_points = tuple([ ( random.randint(0, 10), random.randint(0, 10) ) for k in range(random.randint(4, 7)) ])
    degree = 3
    N = 100

    bspline = Bspline(control_points, degree)

    points = map(bspline.curve, (i / N for i in xrange(N + 1)))
    x, y = ([p[j] for p in points] for j in (0, 1))
    plt.plot(x, y, 'b-')
    x, y = ([p[j] for p in control_points] for j in (0, 1))
    plt.plot(x, y, 'ro-')

    plt.grid(True)
    plt.show()
