import numpy as np


def optimize(angles, stepSize, T, reg):
    angles, triangles = getTriangles(angles)
    orgAngles = angles
    for i in range(T):
        angles,triangles = getTriangles(angles)

        gradient = getGradient(orgAngles, angles, triangles, reg)
        for key in angles:
            angles[key] = angles[key] - gradient[key]*stepSize

    return angles, triangles

def getAngles():
    angles = dict()
    angles[0, 1, 2] = 50
    angles[0, 2, 3] = 70
    angles[1, 2, 0] = 70
    angles[2, 1, 0] = 79
    angles[2, 0, 3] = 81
    angles[3, 2, 0] = 50


    angles[0, 3, 4] = 50
    angles[0, 2, 4] = 50
    angles[2, 0, 4] = 30
    angles[2, 3, 4] = 45
    angles[3, 0, 4] = 35
    angles[3, 2, 4] = 30
    angles[4, 2, 3] = 30
    angles[4, 0, 3] = 40
    angles[4, 0, 2] = 50
    angles[5, 0, 2] = 50

    return angles

def getTriangles(angles):

    n = 6
    triangles = dict()
    for home in angles:
        for first in angles:
            if (first[0] == home[1] and first[1] == home[0] and first[2] == home[2]) or (first[0] == home[1] and first[1] == home[2] and first[2] == home[0]):
                for second in angles:
                    if (second[0] == home[2] and second[1] == home[0] and second[2] == home[1]) or (second[0] == home[2] and second[1] == home[1] and second[2] == home[0]):
                        triangles[home] = angles[home] + angles[first] + angles[second]


    """
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i!= k:
                    if (i, j, k) in angles:
                        if (j, k, i) in angles:
                            if (k, i, j) in angles:
                                triangles[i ,j ,k] = angles[i,j,k] + angles[j, k, i] + angles[k, i, j]
                            if (k, j, i) in angles:
                                triangles[i ,j ,k] = angles[i,j,k] + angles[j, k, i] + angles[k, j, i]
                        if (j, i, k) in angles:
                            if (k, i, j) in angles:
                                triangles[i, j, k] = angles[i, j, k] + angles[j, i, k] + angles[k, i, j]
                            if (k, j, i) in angles:
                                triangles[i, j, k] = angles[i, j, k] + angles[j, i, k] + angles[k, j, i]
    """
    #Done: clean up angles not in triangles
    for key in list(angles):
        if key not in triangles:
            print("Angle " + str(key) + " " + str(angles[key]) + " removed")
            angles.pop(key)
    return angles, triangles

def getCost(triangles):
    cost = 0
    for key in triangles:
        cost += np.square(triangles[key]-200)
    return cost

def getGradient(orgAngles, angles, triangles,reg):
    gradient = dict()
    for key in angles:
        triangleAngle = triangles[key]
        grad = triangleAngle*2 - 400# + reg * abs(orgAngles[key]-angles[key])
        gradient[key] = grad

    return gradient

angles, triangles = optimize(getAngles(), 0.1 ,100, 1)
print(angles)
print(triangles)