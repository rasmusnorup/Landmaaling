import numpy as np
import LengthFinder as LN

def findCoordinates(azimuths, leng, origo):
    azimuths = LN.convertToRadians(azimuths)
    lengths = dict()
    for len in leng:
        if len[0] + len[2] not in lengths:
            lengths[len[0] + len[2]] = leng[len]
    queue = [origo]
    coordinatesX = dict()
    coordinatesY = dict()
    coordinatesX[origo] = 0.0
    coordinatesY[origo] = 0.0
    while queue:
        point = queue.pop()
        for key in azimuths:
            if key[0] == point:
                if key[1] not in coordinatesX:
                    coordinatesX[key[1]] = coordinatesX[point] + np.cos(azimuths[key]) * lengths[key]
                    coordinatesY[key[1]] = coordinatesY[point] + np.sin(azimuths[key]) * lengths[key]
                    queue.append(key[1])
    return coordinatesX, coordinatesY


def findAllAzimuths(angles, known, azimuth):
    queue = [known[0]]
    azimuths = dict()
    azimuths[known] = azimuth
    azimuths[known[1]+known[0]] = np.mod(azimuth + 200, 400)
    while queue:
        point = queue.pop()
        for temp in azimuths:
            if temp[0] == point:
                known = temp
        azi = findAzimuths(angles, known, azimuths[known])
        for key in azi:
            if key not in azimuths:
                azimuths[key] = azi[key]
                if azi[key] > 200:
                    azimuths[key[1]+key[0]] = azi[key] - 200
                else:
                    azimuths[key[1] + key[0]] = azi[key] + 200
                queue.append(key[1])
    return azimuths

def findAzimuths(angles, known, azi):
    point = known[0]
    azimuths = dict()
    for key in angles:
        if key[1] == point:
            if key[0] == known[1]:
                azimuths[key[1]+key[2]] = np.mod(azi + angles[key],400)
    return azimuths