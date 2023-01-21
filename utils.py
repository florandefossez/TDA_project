import numpy as np


def anulus(n_points, r=1, width=0.5):
    points = np.random.rand(n_points)*2*np.pi
    points = np.array([np.cos(points), np.sin(points)])*(np.random.rand(n_points)*width + r)
    points = np.transpose(points)
    return points

def torus(n_points, r=5, width=0.5):
    a1 = np.random.rand(n_points)*2*np.pi
    a2 = np.random.rand(n_points)*2*np.pi
    points = width*np.cos(a2) + r
    points = np.array([points*np.cos(a1), points*np.sin(a1), width*np.sin(a2)])
    return np.transpose(points)
