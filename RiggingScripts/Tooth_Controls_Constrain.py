import maya.cmds as mc

for x in range(1, 30):
    if x < 10:
        mc.select("Tooth_0" + str(x))
        curPoint = mc.xform(query=True, translation=True, worldSpace=True)
        mc.select("ctrl_Tooth_0" + str(x))
        mc.move(curPoint[0], curPoint[1], curPoint[2], "ctrl_Tooth_0" + str(x) + ".scalePivot",
                "ctrl_Tooth_0" + str(x) + ".rotatePivot", absolute=True)

        mc.select("Tooth_0" + str(x), tgl=True)
        mc.parentConstraint(mo=True)
    else:
        mc.select("Tooth_" + str(x))
        curPoint = mc.xform(query=True, translation=True, worldSpace=True)
        mc.select("ctrl_Tooth_" + str(x))
        mc.move(curPoint[0], curPoint[1], curPoint[2], "ctrl_Tooth_" + str(x) + ".scalePivot",
                "ctrl_Tooth_" + str(x) + ".rotatePivot", absolute=True)

        mc.select("Tooth_" + str(x), tgl=True)
        mc.parentConstraint(mo=True)