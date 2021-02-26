import maya.cmds as mc
import math

wid = 2
dist = 0.1
hig = 1

crv = "curve1"

for i in range(0,20):
    dist = 0 + 0.01*(i%2)
    while dist < 1:
        tan = mc.pointOnCurve(crv,t=1,top=1,pr=dist)
        mag = math.sqrt(tan[0]*tan[0]+tan[1]*tan[1]+tan[2]*tan[2])
        rot = math.atan2(tan[0],tan[2])
        p = mc.pointOnCurve(crv,top=1,pr=dist)
        #print(p)
        c = mc.polyCube(w=wid,h=hig)
        mc.rotate(0,math.degrees(rot)+90,0)
        mc.move(p[0],i*1.05+p[1],p[2])
        dist = dist + 0.3/mag