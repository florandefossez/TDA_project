import numpy as np


def anulus(n_points, r=1, width=0.5):
    points = np.random.rand(n_points)*2*np.pi
    points = np.array([np.cos(points), np.sin(points)])*(np.random.rand(n_points)*width + r)
    points = np.transpose(points)
    return points