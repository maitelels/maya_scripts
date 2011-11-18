#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_clusterCurveComponent;reload(tim_clusterCurveComponent);tim_clusterCurveComponent.main()

import maya.cmds as mc
import maya.mel as mm

def main():
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
		print "here"
		cluster = mc.cluster(n=clusname)
	
		location = mc.xform(cluster, q=1, ws=1, sp=1)
		print location
		locator = mc.spaceLocator(n=locname, p=(location[0], location[1], location[2]))
		mc.xform(locator, cp=1)
		set_vis = clusname+"Handle.visibility"
		mc.setAttr(set_vis, 0)
		mc.parent(cluster, locator)
		mc.parent(locator, grp)
		
		shape = mc.listRelatives(locator)
		mc.setAttr((shape[0]+".overrideEnabled"),1)
		mc.setAttr((shape[0]+".overrideColor"),17)
		
