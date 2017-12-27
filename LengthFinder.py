import numpy as np
import AngleOptimizer as Opt

def findAllLengths(angles, triangles, known, length):
    lengths = dict()
    lengths[known] = length
    queue = [known]
    while queue:
        known = queue.pop()
        ang = dict()
        ang[known] = angles[known]
        ang[known[1:3]+known[0]] = angles[known[1:3]+known[0]]
        ang[known[2]+known[0:2]] = angles[known[2]+known[0:2]]
        newLengths = findTriangleLengths(ang, known, lengths[known])
        for key in newLengths:
            if key not in lengths:
                lengths[key] = newLengths[key]

                for temp in angles:
                    if key[2]+key[1] in temp and temp not in lengths and key[2]+key[1] == temp[1:3]:
                        queue.append(temp)
                        lengths[temp] = newLengths[key]
                        print(queue)
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

"""
a = dict()
a["ACB"] = 50
a["CBA"] = 90
a["BAC"] = 60

a["CDB"] = 45
a["DBC"] = 100
a["BCD"] = 55

#lengths = findTriangleLengths(a, "BAC", 100)
#print(lengths)
triangles = Opt.getTriangles(a)
lengths = findAllLengths(a, triangles, "BAC", 100)
print(lengths)
"""
