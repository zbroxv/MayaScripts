import maya.cmds as mc
import math

numSleepers = 250
inputCurve = 'curve1'

mc.select(inputCurve)
curveString = mc.duplicate(rr=True)
curveName = curveString[0]

mc.rebuildCurve(curveName, s=40)

sleepers = []
for i in range(0, numSleepers - 1):
    dist = (1.0 / numSleepers) * i
    pos = mc.pointOnCurve(curveName, pr=dist, top=True)
    tan = mc.pointOnCurve(curveName, pr=dist, t=True, top=True)
    rot = math.degrees(math.atan2(tan[0], tan[2]))
    curCube = mc.polyCube(w=8, h=0.5)
    mc.move(pos[0], pos[1], pos[2])
    mc.rotate(0, rot, 0)
    sleepers.append(curCube[0])
sleeperGroup = mc.group(sleepers, n='Sleepers')

pos = mc.pointOnCurve(curveName, pr=0, top=True)
tan = mc.pointOnCurve(curveName, pr=0, t=True, top=True)
rot = math.degrees(math.atan2(tan[0], tan[2]))
rail = mc.polyPlane(sx=1, sy=1)
mc.move(pos[0], pos[1], pos[2])
mc.rotate(90, rot, 0)
mc.select(rail[0] + '.f[0]', curveName)
div = numSleepers * 2
mc.polyExtrudeFacet(rail[0] + '.f[0]', inputCurve=curveName, divisions=div)

extrudeFaces = []
for i in range(0, div):
    curFace = rail[0] + '.f[' + str(2 + div + i) + ']'  # left side faces
    extrudeFaces.append(curFace)
for i in range(0, div):
    curFace = rail[0] + '.f[' + str(2 + (div * 3) + i) + ']'  # right side faces
    extrudeFaces.append(curFace)
mc.polyExtrudeFacet(extrudeFaces, thickness=1.6)

edgeForCurveLeft = []
for i in range(0, div):
    curFace = rail[0] + '.e[' + str(10 + (div * 6) + (i * 5)) + ']'  # left side faces
    edgeForCurveLeft.append(curFace)
mc.select(edgeForCurveLeft)
leftCurve = mc.polyToCurve()

pos = mc.pointOnCurve(leftCurve[0], pr=0, top=True)
tan = mc.pointOnCurve(leftCurve[0], pr=0, t=True, top=True)
rot = math.degrees(math.atan2(tan[0], tan[2]))
leftRail = mc.polyPlane(sx=1, sy=1)
mc.move(pos[0], pos[1], pos[2])
mc.rotate(90, rot, 0)
mc.select(leftRail[0] + '.f[0]', leftCurve[0])
div = numSleepers * 2
mc.polyExtrudeFacet(leftRail[0] + '.f[0]', inputCurve=leftCurve[0], divisions=div)

edgeForCurveRight = []
for i in range(0, div):
    curFace = rail[0] + '.e[' + str(16 + (div * 11) + (i * 5)) + ']'  # right side faces
    edgeForCurveRight.append(curFace)
mc.select(edgeForCurveRight)
rightCurve = mc.polyToCurve()

pos = mc.pointOnCurve(rightCurve[0], pr=0, top=True)
tan = mc.pointOnCurve(rightCurve[0], pr=0, t=True, top=True)
rot = math.degrees(math.atan2(tan[0], tan[2]))
rightRail = mc.polyPlane(sx=1, sy=1)
mc.move(pos[0], pos[1], pos[2])
mc.rotate(90, rot, 0)
mc.select(rightRail[0] + '.f[0]', rightCurve[0])
div = numSleepers * 2
mc.polyExtrudeFacet(rightRail[0] + '.f[0]', inputCurve=rightCurve[0], divisions=div)

mc.group(leftRail, rightRail, sleeperGroup, n='Track')

mc.delete(leftRail[0],rightRail[0], constructionHistory=True)
mc.delete(rail[0], leftCurve[0], rightCurve[0])
mc.delete(curveName)