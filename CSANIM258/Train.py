import maya.cmds as mc
import random

### VARIABLES ###

numSleepers = int(raw_input())
numCars = int(raw_input())
distSleepers = 2.5
rotAmp = 4
trainSpeed = 10


def MakeTrack():
    # Detail geometry on the sleepers
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
    singleSleeper = mc.group(sleeper)

    # Making Sleepers
    sleepers = []
    sleepers.append(singleSleeper)

    negSleeperNum = 20 + (numCars * 17)

    if numSleepers > negSleeperNum:
        for i in range(1, negSleeperNum):
            curSleeper = mc.duplicate(rr=True)
            mc.move(-distSleepers * i, 0, 0)
            sleeperCurve = random.randrange(-rotAmp, rotAmp)
            mc.rotate(0, sleeperCurve, 0)
            sleepers.extend(curSleeper)


        rail1 = mc.polyCube(w=negSleeperNum * distSleepers, h=1, d=0.4)
        mc.move(-((negSleeperNum - 1) * distSleepers) / 2, 0.6, 3)
        sleepers.append(rail1[0])

        rail2 = mc.duplicate(rr=True)
        mc.move(0, 0, -6, r=True)
        sleepers.append(rail2[0])

        rail3 = mc.polyCube(w=negSleeperNum * distSleepers, h=0.2, d=0.59)
        mc.move(-((negSleeperNum - 1) * distSleepers) / 2, 1.1, 3.1)
        sleepers.append(rail3[0])

        rail4 = mc.duplicate(rr=True)
        mc.move(0, 0, -6.2, r=True)
        sleepers.append(rail4[0])

        posSleeperNum = numSleepers - negSleeperNum
        mc.select(singleSleeper)

        for i in range(1, posSleeperNum):
            curSleeper = mc.duplicate(rr=True)
            mc.move(distSleepers * i, 0, 0)
            sleeperCurve = random.randrange(-rotAmp, rotAmp)
            mc.rotate(0, sleeperCurve, 0)
            sleepers.extend(curSleeper)

        rail5 = mc.polyCube(w=posSleeperNum * distSleepers, h=1, d=0.4)
        mc.move(((posSleeperNum - 1) * distSleepers) / 2, 0.6, 3)
        sleepers.append(rail5[0])

        rail6 = mc.duplicate(rr=True)
        mc.move(0, 0, -6, r=True)
        sleepers.append(rail6[0])

        rail7 = mc.polyCube(w=posSleeperNum * distSleepers, h=0.2, d=0.59)
        mc.move(((posSleeperNum - 1) * distSleepers) / 2, 1.1, 3.1)
        sleepers.append(rail7[0])

        rail8 = mc.duplicate(rr=True)
        mc.move(0, 0, -6.2, r=True)
        sleepers.append(rail8[0])

    else:
        for i in range(1, numSleepers):
            curSleeper = mc.duplicate(rr=True)
            mc.move(-distSleepers * i, 0, 0)
            sleeperCurve = random.randrange(-rotAmp, rotAmp)
            mc.rotate(0, sleeperCurve, 0)
            sleepers.extend(curSleeper)

        rail1 = mc.polyCube(w=numSleepers * distSleepers, h=1, d=0.4)
        mc.move(-((numSleepers - 1) * distSleepers) / 2, 0.6, 3)
        sleepers.append(rail1[0])

        rail2 = mc.duplicate(rr=True)
        mc.move(0, 0, -6, r=True)
        sleepers.append(rail2[0])

        rail3 = mc.polyCube(w=numSleepers * distSleepers, h=0.2, d=0.59)
        mc.move(-((numSleepers - 1) * distSleepers) / 2, 1.1, 3.1)
        sleepers.append(rail3[0])

        rail4 = mc.duplicate(rr=True)
        mc.move(0, 0, -6.2, r=True)
        sleepers.append(rail4[0])

    # Group the whole rail
    finalRail = mc.group(sleepers, n="Rail")

    return finalRail


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

    return finalEngine


def MakeCars():
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

    carList = []
    carList.append(groupedCar)

    # Number of Cars

    for i in range(1, numCars):
        curCar = mc.duplicate(rr=True, ic=True)
        mc.move(-42.81, 0, 0, r=True)
        carList.append(curCar[0])

    return carList


### MAIN ###

if numSleepers > 0:
    MakeTrack()
engine = MakeEngine()
if numCars > 0:
    cars = MakeCars()
    train = mc.group(engine, cars, n="Train")
    mc.expression(s="translateX = time *"+str(trainSpeed)+";", o=train)
else:
    mc.expression(s="translateX = time *"+str(trainSpeed)+";", o=engine)
