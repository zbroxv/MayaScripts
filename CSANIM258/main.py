import maya.cmds as mc
import math

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

MakeEngine()