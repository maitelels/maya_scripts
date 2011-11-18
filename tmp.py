import pymel.core as pm

pm.ikHandle(startJoint="center1", endEffector="center13",  sol="ikSplineSolver",ns=3)
pm.ikHandle(startJoint="left1", endEffector="left13",  sol="ikSplineSolver",ns=3)
pm.ikHandle(startJoint="right1", endEffector="right13",  sol="ikSplineSolver",ns=3)

###########
# 
###########

################
# open & fan
import pymel.core as pm; pages = 33; book = pm.ls('world_ctrl')[0]
pm.setAttr(book+".openL", 90); pm.setAttr(book+".openR", 90)
pm.setAttr(book+"."+('page'+"0"), -10)
degree = 20.0/pages
for page in range(pages):
    value = -10+ (float(page)*degree)
    print page, value
    pm.setAttr(book+"."+('page'+str(page)),value )

################
# close & reset
import pymel.core as pm; pages = 33; book = pm.ls('world_ctrl')[0]
pm.setAttr(book+".openL", 0); pm.setAttr(book+".openR", 0)
for page in range(pages):
    pm.setAttr(book+"."+('page'+str(page)), 0 )

################
# hero 1
import pymel.core as pm; pages = 33; book = pm.ls('world_ctrl')[0]
pm.setAttr(book+".openL", 90); pm.setAttr(book+".openR", 90)
for page in range(pages):
    pm.setAttr(book+"."+('page'+str(page)), -10)
pm.setAttr(book+"."+('page'+"6"), 0)

################
# hero 2
import pymel.core as pm; pages = 33; book = pm.ls('world_ctrl')[0]
pm.setAttr(book+".openL", 90); pm.setAttr(book+".openR", 90)
for page in range(pages):
    pm.setAttr(book+"."+('page'+str(page)), -10)
pm.setAttr(book+"."+('page'+"19"), 0)



###########
# connect main speaker ctrl to speaker ctrls
###########
import pymel.core as pm

speakerCtrls = pm.ls("*:*:*speaker_ctrl")
mainCtrl = pm.ls("BOXENANIMATION")[0]

for ctrl in speakerCtrls:
    pm.connectAttr( mainCtrl+".tz", ctrl+".tz")
    pm.connectAttr( mainCtrl+".rx", ctrl+".rx")
    pm.connectAttr( mainCtrl+".speakerScaleX", ctrl+".speakerScaleX")
    pm.connectAttr( mainCtrl+".speakerScaleY", ctrl+".speakerScaleY")
    pm.connectAttr( mainCtrl+".membraneAction", ctrl+".membraneAction")
    pm.connectAttr( mainCtrl+".speakerAction", ctrl+".speakerAction")
    
    
##########
# shift anim
########### 
import pymel.core as pm

ctrl = pm.ls("SPEAKERANIMATION")
pm.select(ctrl[0], r=1)

allAnimCurves = []

animCurveTL = pm.listConnections(t="animCurveTL")
animCurveTA = pm.listConnections(t="animCurveTA")
animCurveTU = pm.listConnections(t="animCurveTU")

for crv in animCurveTL:
    allAnimCurves.append(crv)
    
for crv in animCurveTA:
    allAnimCurves.append(crv)

for crv in animCurveTU:
    allAnimCurves.append(crv)
    
for crv in allAnimCurves:
    print crv
    pm.selectKey(crv)
    pm.keyframe(animation="keys", option="over", relative=1, timeChange=(0 + 288))




#############
# reset speakers timing
#############

import pymel.core as pm

ctrl = pm.ls("SPEAKERANIMATION")
pm.select(ctrl[0], r=1)

allAnimCurves = []

animCurveTL = pm.listConnections(t="animCurveTL")
animCurveTA = pm.listConnections(t="animCurveTA")
animCurveTU = pm.listConnections(t="animCurveTU")

for crv in animCurveTL:
    allAnimCurves.append(crv)
    
for crv in animCurveTA:
    allAnimCurves.append(crv)

for crv in animCurveTU:
    allAnimCurves.append(crv)
    
pm.selectKey(allAnimCurves[0], index=(0,0))
resetValue = pm.keyframe(q=1)[0]

for crv in allAnimCurves:
    print crv
    pm.selectKey(crv)
    pm.keyframe(animation="keys", option="over", relative=1, timeChange=(0 + resetValue))


