import csv

import numpy as np
import Data

def optimize(angles, stepSize, T, reg):
    triangles = getTriangles(angles)
    orgAngles = angles
    for i in range(T):
        triangles = getTriangles(angles)

        gradient = getGradient(orgAngles, angles, triangles, reg)
        for key in angles:
            angles[key] = angles[key] - gradient[key]*stepSize
    return angles, triangles

def getAngles2():
    angles = dict()
    angles[0, 2, 3] = 60
    angles[0, 3, 1] = 60
    angles[1, 0, 3] = 60
    angles[1, 3, 2] = 60
    angles[2, 1, 3] = 60
    angles[2, 3, 0] = 60
    angles[3, 1, 0] = 160
    angles[3, 2, 1] = 120
    angles[3, 0, 2] = 120

    #outer angles:
    angles[0, 1, 2] = 400-120
    angles[1, 2, 0] = 400-120
    angles[2, 0, 1] = 400-120

    return angles

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
    triangles = dict()
    for home in angles:
        if angles[home] < 200:
            for first in angles:
                if angles[first] < 200:
                    if first[0] == home[1] and first[1] == home[2] and first[2] == home[0]:
                        for second in angles:
                            if angles[second] < 200:
                                if (second[0] == home[2] and second[1] == home[0] and second[2] == home[1]):
                                    triangles[home] = angles[home] + angles[first] + angles[second]
    """
    n = 6
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
    
    #Done: clean up angles not in triangles
    for key in list(angles):
        if key not in triangles:
            print("Angle " + str(key) + " " + str(angles[key]) + " removed")
            angles.pop(key)
    """
    return triangles

def getCost(triangles):
    cost = 0
    for key in triangles:
        cost += np.square(triangles[key]-200)
    return cost

def getGradient(orgAngles, angles, triangles,reg):
    gradient = dict()
    points = getPoints(angles)
    for key in angles:
        triangleAngle = 200
        if key in triangles:
            triangleAngle = triangles[key]
        point = points[key[1]]
        grad = triangleAngle*2 - 400 + point*2 - 800 #+ reg * abs(orgAngles[key]-angles[key])
        gradient[key] = grad

    return gradient

def getPoints(angles):
    points = dict()
    for key in angles:
        if key[1] not in points:
            points[key[1]] = 0
        points[key[1]] = points[key[1]] + angles[key]

    return points

def getError(triangles, points):
    triError = sum([abs(triangles[key]-200) for key in triangles])
    pointError = sum([abs(points[key]-400) for key in points])
    return triError, pointError

angles, triangles = optimize(Data.getAngles(), 0.05 , 100, 10)
print(angles)
print(triangles)
print(getPoints(angles))
triError, pointError = getError(triangles, getPoints(angles))
print(triError)
print(pointError)


triError, pointError = getError(getTriangles(Data.getAngles()), getPoints(Data.getAngles()))
print(triError)
print(pointError)

"""
with open('result2.csv', 'w', newline='') as csvfile:
    fieldnames = ['Navn', 'Vinkel']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')

    writer.writeheader()
    for key, val in angles.items():
        writer.writerow({'Navn': key , 'Vinkel' : val})
"""