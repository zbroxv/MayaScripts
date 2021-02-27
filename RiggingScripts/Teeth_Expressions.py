import maya.cmds as mc
import random

for x in range(1, 30):
    if x < 10:
        mc.expression(s="ctrl_Tooth_0" + str(x) + ".rotateZ = sin(time * 50 + " + str(
            random.random()) + ") * ctrl_main.teethJitterAmp * (ctrl_main.teethJitterSwitch / 10.0);")

    else:
        mc.expression(s="ctrl_Tooth_" + str(x) + ".rotateZ = sin(time * 50 + " + str(
            random.random()) + ") * ctrl_main.teethJitterAmp * (ctrl_main.teethJitterSwitch / 10.0);")