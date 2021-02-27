import maya.cmds as mc

for x in range(1, 30):
    if x < 10:
        mc.select("Tooth_0" + str(x))
        curPoint = mc.xform(query=True, translation=True, worldSpace=True)
        mc.group("ctrl_Tooth_0" + str(x), name="grp_retract_0"+str(x))
        mc.move(curPoint[0], curPoint[1], curPoint[2], "grp_retract_0" + str(x) + ".scalePivot",
                "grp_retract_0" + str(x) + ".rotatePivot", absolute=True)

    else:
        mc.select("Tooth_" + str(x))
        curPoint = mc.xform(query=True, translation=True, worldSpace=True)
        mc.group("ctrl_Tooth_" + str(x), name="grp_retract_"+str(x))
        mc.move(curPoint[0], curPoint[1], curPoint[2], "grp_retract_" + str(x) + ".scalePivot",
                "grp_retract_" + str(x) + ".rotatePivot", absolute=True)
