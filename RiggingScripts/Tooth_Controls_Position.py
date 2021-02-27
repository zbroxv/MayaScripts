import maya.cmds as mc

for x in range(1,30):
    if x < 10:
        mc.select("grp_ctrl_tooth_0"+str(x))
        mc.select("Tooth_0"+str(x), tgl=True)
        mc.parent()
        mc.rotate(0,0,90)
        mc.setAttr("grp_ctrl_tooth_0"+str(x)+".translateX", 0)
        mc.setAttr("grp_ctrl_tooth_0"+str(x)+".translateY", 0)
        mc.setAttr("grp_ctrl_tooth_0"+str(x)+".translateZ", 0)
        mc.select("grp_ctrl_tooth_0"+str(x))
        mc.select("Tooth_Controls", tgl=True)
        mc.parent()
    else:
        mc.select("grp_ctrl_tooth_"+str(x))
        mc.select("Tooth_"+str(x), tgl=True)
        mc.parent()
        mc.rotate(0,0,90)
        mc.setAttr("grp_ctrl_tooth_"+str(x)+".translateX", 0)
        mc.setAttr("grp_ctrl_tooth_"+str(x)+".translateY", 0)
        mc.setAttr("grp_ctrl_tooth_"+str(x)+".translateZ", 0)
        mc.select("grp_ctrl_tooth_"+str(x))
        mc.select("Tooth_Controls", tgl=True)
        mc.parent()