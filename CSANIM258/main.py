import maya.cmds as mc
import math
import random

distSleepers = 4
inputCurve = 'curve1'
startFrame = 0
trainSpeed = 40
numCars = int(raw_input())
rotAmp = 4

mc.select(inputCurve)
curveString = mc.duplicate(rr=True, n='AnimationCurve')
curveName = curveString[0]
mc.rebuildCurve(curveName, s=40, kr=0)
curveLength = mc.arclen(curveName)
trackSegmentLength = 10 * distSleepers
numSleepers = curveLength / distSleepers

def MakeSleeper():
    detailGeo = []

    cube01 = mc.polyCube(w=0.6, h=.1, d=.6)
    mc.move(0, 0.2, 3.5)
    detailGeo.append(cube01[0])

    cube02 = mc.polyCube(w=0.6, h=.1, d=.6)
    mc.move(0, 0.2, 3.5)
    detailGeo.append(cube02[0])

    cube03 = mc.polyCube(w=0.6, h=.26, d=.137)
    mc.move(0, 0.24, 3.34)
    detailGeo.append(cube03[0])

    cylinder01 = mc.polyCylinder()
    mc.scale(0.13, 0.13, 0.13)
    mc.move(0.15, 0.16, 3.6)
    detailGeo.append(cylinder01[0])

    cylinder02 = mc.polyCylinder()
    mc.scale(0.13, 0.13, 0.13)
    mc.move(-0.15, 0.16, 3.6)
    detailGeo.append(cylinder02[0])

    cylinder03 = mc.polyCylinder()
    mc.scale(0.09, 0.13, 0.09)
    mc.move(0.15, 0.3, 3.6)
    detailGeo.append(cylinder03[0])

    cylinder04 = mc.polyCylinder()
    mc.scale(0.09, 0.13, 0.09)
    mc.move(-0.15, 0.3, 3.6)
    detailGeo.append(cylinder04[0])

    cylinder05 = mc.polyCylinder()
    mc.rotate(0, 0, 90)
    mc.scale(0.09, 0.324, 0.09)
    mc.move(0, 0.363, 3.345)
    detailGeo.append(cylinder05[0])

    # Duplicating the detail geometry
    detail = mc.group(detailGeo)
    detailDuplicate = mc.duplicate(rr=True)
    mc.scale(1, 1, -1, r=True)
    mc.move(0, 0, -7, r=True)

    # Sleeper Board
    board = mc.polyCube(w=1, h=.3, d=10)

    # Grouping single sleeper
    sleeper = []
    sleeper.append(detail)  # to add the string 'group1' to a list you have to use append
    sleeper.extend(detailDuplicate)  # you have to extend the duplicate to pull it out the string it is formed in
    sleeper.append(board[0])
    singleSleeper = mc.group(sleeper, n="Sleeper1")
    mc.rotate(0, 90, 0)

    return singleSleeper


def MakeRailPiece(curve="", height=1.0, width=1.0):
    pos = mc.pointOnCurve(curve, pr=0, top=True)
    tan = mc.pointOnCurve(curve, pr=0, t=True, top=True)
    rot = math.degrees(math.atan2(tan[0], tan[2]))
    railPiece = mc.polyPlane(w=width, h=height, sx=1, sy=1)
    mc.move(pos[0], pos[1], pos[2])
    mc.rotate(90, rot, 0)
    mc.select(railPiece[0] + '.f[0]', leftCurve[0])
    div = distSleepers * 4
    mc.polyExtrudeFacet(railPiece[0] + '.f[0]', inputCurve=curve, divisions=div)
    mc.delete(railPiece[0], constructionHistory=True)

    return railPiece[0]


def CutRailPieces(curve="", height=1.0, width=1.0):
    mc.delete(curve, ch=True)
    railGeoList = []
    tempCurCurve = [curve]
    mc.rebuildCurve(curve, s=curveLength / trackSegmentLength * 5)

    finalSegmentCurve = mc.detachCurve(curve + ".ep[" + str(int(curveLength / trackSegmentLength * 5) - 5) + "]",
                                       rpo=False, ch=False)
    finalSegmentGeo = MakeRailPiece(curve=finalSegmentCurve[1],  width=width, height=height)
    railGeoList.append(finalSegmentGeo)
    mc.delete(finalSegmentCurve[0], finalSegmentCurve[1])
    deleteGroup = []
    for x in range(int(curveLength / trackSegmentLength)):
        tempCurCurve = mc.detachCurve(tempCurCurve[0] + ".ep[5]", rpo=True, ch=False)
        curRail = MakeRailPiece(curve=tempCurCurve[1], width=width, height=height)
        railGeoList.append(curRail)
        deleteGroup.append(tempCurCurve[0])
        print "iteration"
    mc.delete(deleteGroup)

    return railGeoList


def MakeWheel(radius=3.6):  # Function returns group name for a wheel
    myListOfRotValues = range(0, 360, 20)
    wheel = []
    x = 0
    for curCyl in myListOfRotValues:
        curSpoke = mc.polyCylinder(r=0.1, h=radius)
        wheel.append(curSpoke[0])
        mc.move(0, radius/2, 0)
        mc.move(0, 0, 0, curSpoke[0] + ".scalePivot", curSpoke[0] + ".rotatePivot")
        mc.rotate(20 * x, 0, 0)
        x += 1

    wheelCenter = mc.polyCylinder(ax=(1, 0, 0))
    wheel.append(wheelCenter[0])
    mc.scale(0.22, 0.6, 0.6)

    wheelEdge = mc.polyTorus(r=radius, sr=0.3, sx=40, sy=5, ax=(1, 0, 0))
    mc.scale(0.537, 1, 1)
    wheel.append(wheelEdge[0])

    finalWheel = mc.group(wheel)

    if trainSpeed > 0:
        circumference = 2 * 3.14 * radius
        wheelRotationTime = (circumference / trainSpeed)
        mc.expression(s="rotateX = time * (360 / " + str(wheelRotationTime) + ");", o=finalWheel)

    return finalWheel


def MakeEngine():
    car01 = []
    engine = []

    engineBody = mc.polyCylinder(ax=(1, 0, 0))
    engine.append(engineBody[0])
    mc.polyExtrudeFacet(engineBody[0] + ".f[21]", thickness=1)
    mc.scale(0.8, 0.8, 0.8, r=True)
    mc.polyExtrudeFacet(engineBody[0] + ".f[21]", thickness=6)
    mc.select(engineBody[0], r=True)
    mc.scale(2.7, 2.7, 2.7, r=True)
    mc.move(-30, 10, 0)

    engineNub01 = mc.polyCylinder()
    engine.append(engineNub01[0])
    mc.move(-18, 12, 0)

    engineNub02 = mc.polyCylinder(h=4)
    engine.append(engineNub02[0])
    mc.move(-23, 13, 0)

    engineSteam = mc.polyCylinder()
    engine.append(engineSteam[0])
    mc.scale(1.65, 1.65, 1.65)
    mc.move(-14, 12, 0)
    mc.polyExtrudeFacet(engineSteam[0] + ".f[21]", thickness=0.3)
    mc.select(engineSteam[0] + ".f[21]", r=True)
    mc.scale(1.5, 1.5, 1.5, r=True)
    mc.polyExtrudeFacet(engineSteam[0] + ".f[21]", thickness=2)

    engineCircle01 = mc.polyCylinder(ax=(1, 0, 0))
    engine.append(engineCircle01[0])
    mc.move(-24.87, 10.04, 0)
    mc.scale(0.42, 2.09, 2.09)

    engineCircle02 = mc.polyCylinder(ax=(1, 0, 0))
    engine.append(engineCircle02[0])
    mc.move(-20.27, 10.04, 0)
    mc.scale(0.42, 2.09, 2.09)

    engineCircle03 = mc.polyCylinder(ax=(1, 0, 0))
    engine.append(engineCircle03[0])
    mc.move(-16.32, 10.04, 0)
    mc.scale(0.42, 2.09, 2.09)

    engineRoof = mc.polyCube()
    engine.append(engineRoof[0])
    mc.move(-33.94, 16.68, 0)
    mc.scale(7.12, 1.21, 10.54)

    engineBox = mc.polyCube()
    engine.append(engineBox[0])
    mc.move(-33.94, 13.13, 0)
    mc.scale(5.07, 6.41, 7.51)
    mc.polyExtrudeFacet(engineBox[0] + ".f[4]")
    mc.select(engineBox[0] + ".f[4]")
    mc.scale(1, 0.45, 0.82)
    mc.move(0, 1, 0, r=True)
    mc.polyExtrudeFacet(engineBox[0] + ".f[4]")
    mc.move(-2, 0, 0, r=True)

    engineBottom = mc.polyCube()
    engine.append(engineBottom[0])
    mc.move(-34, 8.44, 0)
    mc.scale(5.07, 5.07, 5.07)

    engineBaseTop = mc.polyCube()
    engine.append(engineBaseTop[0])
    mc.move(-21.52, 7.58, 0)
    mc.scale(20, 3.01, 2.78)

    engineBaseMid = mc.polyCube()
    engine.append(engineBaseMid[0])
    mc.move(-16.04, 6.811, 0)
    mc.scale(11.26, 0.5, 5.85)

    engineBaseBottom = mc.polyCube()
    engine.append(engineBaseBottom[0])
    mc.move(-21.44, 5.69, 0)
    mc.scale(20.04, 3.06, 2)

    engineAxel = mc.polyCylinder(ax=(0, 0, 1))
    engine.append(engineAxel[0])
    mc.move(-33.64, 5.05, 0)
    mc.scale(0.374, 0.374, 2.977)

    engineAxe2 = mc.polyCylinder(ax=(0, 0, 1))
    engine.append(engineAxe2[0])
    mc.move(-26, 5.05, 0)
    mc.scale(0.374, 0.374, 2.977)

    engineAxe3 = mc.polyCylinder(ax=(0, 0, 1))
    engine.append(engineAxe3[0])
    mc.move(-17.81, 3.77, 0)
    mc.scale(0.25, 0.25, 2.977)

    engineAxe4 = mc.polyCylinder(ax=(0, 0, 1))
    engine.append(engineAxe4[0])
    mc.move(-12.25, 3.77, 0)
    mc.scale(0.25, 0.25, 2.977)

    connectorCube = mc.polyCube()
    engine.append(connectorCube[0])
    mc.move(-35.28, 3.7, 0)
    mc.scale(8.27, 1.04, 3.53)

    connectorTorus = mc.polyTorus(r=1.212, sr=0.25)
    engine.append(connectorTorus[0])
    mc.move(-40.06, 3.71, 0)

    engineGrouped = mc.group(engine)

    car01.append(engineGrouped)

    # Wheels on the engine

    daWheels = []
    whe01 = MakeWheel()
    daWheels.append(whe01)
    mc.move(-33.72, 5.05, 3.14)
    mc.rotate(0, 90, 0)

    whe02 = MakeWheel()
    daWheels.append(whe02)
    mc.move(-25.92, 5.05, 3.14)
    mc.rotate(0, 90, 0)

    whe03 = MakeWheel(radius=2.5)
    daWheels.append(whe03)
    mc.move(-17.81, 3.78, 3.14)
    mc.rotate(0, 90, 0)

    whe04 = MakeWheel(radius=2.5)
    daWheels.append(whe04)
    mc.move(-12.24, 3.78, 3.14)
    mc.rotate(0, 90, 0)

    wheelsRight = mc.group(daWheels)
    wheelsLeft = mc.duplicate(rr=True, ic=True)
    mc.move(0, 0, -6.2, r=True)

    car01.append(wheelsRight)
    car01.extend(wheelsLeft)

    finalEngine = mc.group(car01, n="Engine")
    mc.move(0, -8.596468, 0, finalEngine + '.scalePivot', finalEngine + '.rotatePivot', r=True)

    return finalEngine


def MakeCar():
    trainCarTop = []

    carBody = mc.polyCube()
    trainCarTop.append(carBody[0])
    mc.scale(1.6, 12, 10)

    for x in range(0, 22):
        mc.polyExtrudeFacet(carBody[0] + ".f[4]", thickness=1.6)

    x = 0
    for x in range(0, 12):
        if x == 0:
            faceNum = 0
        else:
            faceNum = 8 * x + 5
        faceString = ".f[" + str(faceNum) + "]"
        mc.polyExtrudeFacet(carBody[0] + faceString, thickness=0.5)
        x += 1

    x = 0
    for x in range(0, 12):
        if x == 0:
            faceNum = 2
        else:
            faceNum = 8 * x + 3
        faceString = ".f[" + str(faceNum) + "]"
        mc.polyExtrudeFacet(carBody[0] + faceString, thickness=0.5)
        x += 1

    mc.select(carBody[0])
    mc.move(-80, 11, 0)

    bottomRail = mc.polyCube()
    trainCarTop.append(bottomRail[0])
    mc.move(-62.27, 3.691, 0)
    mc.scale(40.221, 1.036, 3.53)

    connectorBack = mc.polyTorus(r=1.212, sr=0.25)
    trainCarTop.append(connectorBack[0])
    mc.move(-82.834, 3.71, 0)

    connectorFront = mc.polyTorus(r=1.212, sr=0.25)
    trainCarTop.append(connectorFront[0])
    mc.move(-41.979, 3.71, 0)
    mc.rotate(90, 0, 0)

    theFrikinMain = mc.group(trainCarTop)

    # Wheels on the cars

    carWheels = []
    whe01 = MakeWheel(radius=2.5)
    mc.move(-49.672, 3.78, 3.14)
    mc.rotate(0, 90, 0)
    carWheels.append(whe01)

    whe02 = mc.duplicate(rr=True, ic=True)
    carWheels.extend(whe02)
    mc.move(-55.4, 3.78, 3.14)

    whe03 = mc.duplicate(rr=True, ic=True)
    carWheels.extend(whe03)
    mc.move(-70.123, 3.78, 3.14)

    whe04 = mc.duplicate(rr=True, ic=True)
    carWheels.extend(whe04)
    mc.move(-75.727, 3.78, 3.14)

    wheelsRight = mc.group(carWheels)

    wheelsLeft = mc.duplicate(rr=True, ic=True)
    mc.move(0, 0, -6.245)

    # Group all geometry in car

    theCar = []
    theCar.append(theFrikinMain)
    theCar.append(wheelsRight)
    theCar.extend(wheelsLeft)
    groupedCar = mc.group(theCar, n="Car1")
    mc.move(0, -8.978713, 0, groupedCar + '.scalePivot', groupedCar + '.rotatePivot', r=True)

    return groupedCar


### MAIN ###


sleepers = []
dist = 0
while dist <= curveLength:
    position = mc.pointOnCurve(curveName, pr=dist/curveLength, top=True)
    tangent = mc.pointOnCurve(curveName, pr=dist/curveLength, t=True, top=True)
    roty = math.degrees(math.atan2(tangent[0], tangent[2]))
    rotx = math.degrees(math.atan2(-tangent[1], math.sqrt(tangent[0]*tangent[0]+tangent[2]*tangent[2])))
    curCube = MakeSleeper()
    mc.move(position[0], position[1], position[2])
    mc.rotate(0, roty+90, 0)
    sleeperCurve = random.randrange(-rotAmp, rotAmp)
    mc.rotate(0, sleeperCurve, 0, r=True)
    mc.rotate(rotx, 0, 0, r=True)
    sleepers.append(curCube)
    dist += distSleepers
sleeperGroup = mc.group(sleepers, n='Sleepers')

leftCurve = mc.offsetCurve(curveName, d=3)
mc.move(0, 0.6, 0)
leftCurveTop = mc.duplicate(rr=True)
mc.move(0, 1.1, 0)
leftRail = CutRailPieces(curve=leftCurve[0], width=0.4)
leftRailTop = CutRailPieces(curve=leftCurveTop[0], height=0.2, width=0.7)

rightCurve = mc.offsetCurve(curveName, d=-3)
mc.move(0, 0.6, 0)
rightCurveTop = mc.duplicate(rr=True)
mc.move(0, 1.1, 0)
rightRail = CutRailPieces(curve=rightCurve[0], width=0.4)
rightRailTop = CutRailPieces(curve=rightCurveTop[0], height=0.2, width=0.7)

track = mc.group(leftRail, rightRail, leftRailTop, rightRailTop, sleeperGroup, n='Track')

mc.delete(leftCurve[0], rightCurve[0], leftCurveTop[0], rightCurveTop[0])

engineLength = 15
carLength = 42
engineStart = (engineLength + numCars * carLength) / curveLength
engineEnd = 1 - (engineLength / curveLength)

engine = MakeEngine()
mc.pathAnimation(engine, su=engineStart, eu=engineEnd, stu=startFrame, etu=curveLength/(trainSpeed/24.0), follow=True, c=curveName, fa='x', ua='y')

carList = []
for i in range(0, numCars):
    carStart = (carLength/2 + (carLength * i)) / curveLength
    carEnd = 1 - ((engineLength * 2 + carLength / 2 + carLength * (numCars - i) - carLength) / curveLength)
    curCar = MakeCar()
    mc.pathAnimation(curCar, su=carStart, eu=carEnd, stu=startFrame, etu=curveLength / (trainSpeed / 24.0), follow=True, c=curveName, fa='x',
                     ua='y')
    carList.append(curCar)

cars = mc.group(carList, n="Cars")

mc.group(engine, cars, n='Train')

