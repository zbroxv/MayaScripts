import maya.cmds as mc
import math
import random

curve_name = "curve1"
brickWidth = 2
brickHeight = 1
height = 20  # how many rows tall
rotxAmp = 6
rotzAmp = 3

mc.rebuildCurve(curve_name, s=40)
curveLength = mc.arclen(curve_name)

wall = []
i = 0
while i < height:
    brickRow = []
    dist = 0 + (brickWidth / 2) * i % 2
    while dist < curveLength:
        pos = mc.pointOnCurve(curve_name, pr=dist/curveLength, top=True)
        tangent = mc.pointOnCurve(curve_name, pr=dist/curveLength, top=True, t=True)
        rotation = math.degrees(math.atan2(tangent[0], tangent[2]))+90
        currotx = random.randrange(-rotxAmp, rotxAmp)
        currotz = random.randrange(-rotzAmp, rotzAmp)
        curCube = mc.polyCube(w=brickWidth, h=brickHeight)
        brickRow.append(curCube[0])
        mc.rotate(currotx, rotation, currotz)
        mc.move(pos[0], pos[1], pos[2])
        dist += brickWidth + 0.1
    rowGrp = mc.group(brickRow)
    mc.move(0, (brickHeight + 0.1) * i, 0)
    wall.append(rowGrp)
    i += 1
mc.group(wall, n='Wall')