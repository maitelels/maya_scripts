#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_pageSetupFinish;reload(tim_pageSetupFinish);tim_pageSetupFinish.main()

"""
tim_pageSetupFinish.py

Created by Tim Reischmann on 2011-10-26.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

"""


import pymel.core as pm
import maya.cmds as mc
import maya.mel as mm
from datetime import datetime

#Global Var definitions
proc_name = '## tim_pageSetupFinish: '

def main():
	prefRun()
	
	center = pm.ikHandle(name="centerIK", startJoint="center1", endEffector="center13",  sol="ikSplineSolver",ns=3)
	left = pm.ikHandle(name="leftIK", startJoint="left1", endEffector="left13",  sol="ikSplineSolver",ns=3)
	right = pm.ikHandle(name="rightIK", startJoint="right1", endEffector="right13",  sol="ikSplineSolver",ns=3)
	
	pm.rename(center[2], "center_crv")
	pm.rename(left[2], "left_crv")
	pm.rename(right[2], "right_crv")
	
	clusterGrp_center = clusterCurve("center_crv")
	clusterGrp_left = clusterCurve("left_crv")
	clusterGrp_right = clusterCurve("right_crv")
	
	
	pm.connectAttr("jacketRight1.rz", clusterGrp_right+".rz")
	pm.connectAttr("jacketLeft1.rz", clusterGrp_left+".rz")
	
	pm.parent("center_crv", "rig")
	pm.parent("left_crv", "rig")
	pm.parent("right_crv", "rig")
	
	pm.parent(clusterGrp_center, "world_ctrl")
	pm.parent(clusterGrp_left, "world_ctrl")
	pm.parent(clusterGrp_right, "world_ctrl")
	
	for i in ["centerIK", "leftIK", "rightIK"]:
		pm.setAttr(i+".visibility", 0)
		pm.parent(i, "rig")
	
	for i in ['center_crv','left_crv','right_crv','center_crv_cv0_loc', 'left_crv_cv0_loc', 'right_crv_cv0_loc', 'pageTargets_grp', 'pages_grp', 'jacket_grp']:
		pm.setAttr(i+".visibility", 0)
	

def clusterCurve(curveName):
	mc.select(curveName, r=1)
	mm.eval('selectCurveCV("all");')
	sel = mc.ls(sl=1, fl=1)
	grpname = (sel[0].split('.'))
	grpname = grpname[0]+"_grp"
	grp = mc.group(em=1, n=grpname)
	
	for i in sel:
		iname = i.replace('[', '')
		iname = iname.replace(']','')
		iname = iname.replace('.','_')
		
		locname = iname+"_loc"
		clusname = iname+"_clus"	
		
		mc.select(i, r=1)
		cluster = mc.cluster(n=clusname)
	
		location = mc.xform(cluster, q=1, ws=1, sp=1)
		locator = mc.spaceLocator(n=locname, p=(location[0], location[1], location[2]))
		mc.xform(locator, cp=1)
		set_vis = clusname+"Handle.visibility"
		mc.setAttr(set_vis, 0)
		mc.parent(cluster, locator)
		mc.parent(locator, grp)
		
		shape = mc.listRelatives(locator)
		mc.setAttr((shape[0]+".overrideEnabled"),1)
		mc.setAttr((shape[0]+".overrideColor"),17)
	
	return grp
	
def prefRun():
    '''prefix script run with script name und datetime
    '''
    print '\n\n\n',proc_name,
    print datetime.now(),'##'
