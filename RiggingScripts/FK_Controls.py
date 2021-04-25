#CREATES AND PLACES CONTROL ON SELECTED JOINT
import maya.cmds as mc

joints = mc.ls(sl=True)
print(joints)
jointsSize = len(joints)

for x in range(jointsSize):
    curJoint = joints[x]
    print (curJoint)
    name = str(curJoint)
    curCtrl = mc.circle(n="Ctrl_"+name)
    curGrp = mc.group(curCtrl, n="Ctrl_"+name+"_Grp")
    mc.parent(curGrp, curJoint)
    mc.setAttr(curGrp + ".translateX", 0)
    mc.setAttr(curGrp + ".translateY", 0)
    mc.setAttr(curGrp + ".translateZ", 0)
    mc.setAttr(curGrp + ".rotateX", 0)
    mc.setAttr(curGrp + ".rotateY", 0)
    mc.setAttr(curGrp + ".rotateZ", 0)
    mc.setAttr(curGrp + ".rotateY", 90)
    mc.parent(curGrp, "Ctrl_Base")
    
    
#PARENTCONSTRAINS JOINT TO CONTROL
import maya.cmds as mc

ctrls = mc.ls(sl=True)
ctrlsSize = len(ctrls)

for x in range(ctrlsSize):
    curCtrl = ctrls[x]
    curJoint = curCtrl.replace("Ctrl_", "")
    mc.parentConstraint(curCtrl, curJoint, mo=True, weight=1)
