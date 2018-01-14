import numpy as np


def findAllLengths(angles, known, length):

    lengths = dict()
    queue = [known]
    while queue:
        #print(queue)
        known = queue.pop()
        ang = dict()
        ang[known] = angles[known]
        left = known[1]+known[2]+known[0]
        right = known[2]+known[0]+known[1]

        if left in angles or right in angles:
            if left in angles:
                ang[left] = angles[left]
            else:
                ang[left] = 200 - angles[right] - angles[known]

            if right in angles:
                ang[right] = angles[right]
            else:
                ang[right] = 200 - angles[left] - angles[known]

            if known in lengths:
                length = lengths[known]
            newLengths = findTriangleLengths(ang, known, length)
            for key in newLengths:
                if key not in lengths:
                    lengths[key] = newLengths[key]
                    for temp in angles:
                        if key[2] == temp[0] and key[0] == temp[2] and temp not in lengths:
                            queue.append(temp)
                            if temp not in lengths:
                                lengths[temp] = newLengths[key]
                        if key[0] == temp[0] and key[2] == temp[2] and key[1] != temp[1]:
                            queue.append(temp)
                            if temp not in lengths:
                                lengths[temp] = newLengths[key]
    return lengths


def findTriangleLengths(angles, known, length):
    #angles = dict with "ABC" as key for angles the 3 angles in the triangle, positiv direction.
    #know is the angle opposite the known length, string
    angles = convertToRadians(angles)
    lengths = dict()
    for key in angles:
        lengths[key] = np.sin(angles[key])*length/np.sin(angles[known])
    return lengths


def convertToRadians(angles):
    for key in angles:
        angles[key] = angles[key]/200*np.pi
    return angles


def convertToDegrees(angles):
    for key in angles:
        angles[key] = angles[key]*200/np.pi
    return angles

def makeConcatonatedAngles(angles, times):
    newAngles = angles.copy()
    for i in range(times):
        for start in angles:
            for end in angles:
                if start[1] == end[1] and start[2] == end[0] and start[0] != end[2]:
                    newAngles[start[0:2]+end[2]] = angles[start] + angles[end]
        angles = newAngles.copy()
    return angles


#lengths = findTriangleLengths(a, "BAC", 100)
#print(lengths)
#lengths = findAllLengths(a, "CBA", 100)
#print(lengths)

