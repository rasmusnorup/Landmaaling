import LengthFinder as LF
import AngleOptimizer as Opt
import numpy as np
import Data

"""
a = dict()
a["BAC"] = 50
a["ACK"] = 40
a["KCB"] = 50
a["CBA"] = 60

a["DAC"] = 45
a["ACD"] = 100
a["CDA"] = 55

print(LF.makeConcatonatedAngles(a,1))


angles, triangles = Opt.optimize(Data.getAngles(), 0.05 , 100, 10)
print(angles)
print(triangles)
print(Opt.getPoints(angles))
triError, pointError = Opt.getError(triangles, Opt.getPoints(angles))
print(triError)
print(pointError)


triError, pointError = Opt.getError(Opt.getTriangles(Data.getAngles()), Opt.getPoints(Data.getAngles()))
print(triError)
print(pointError)
"""
angles = Data.getAngles()
#angles, triangles = Opt.optimize(Data.getAngles(), 0.05 , 100, 10)
angles = LF.makeConcatonatedAngles(angles,10)
lengths = LF.findAllLengths(angles, "GJK", 330.0025)
print(lengths)
#print(angles)