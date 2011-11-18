#!/usr/bin/env python
# encoding: utf-8
"""
tim_attachToMotionpath.py

Created by Tim Reischmann on 2011-03-29.
Copyright (c) 2011 Tim Reischmann. All rights reserved.
"""
import maya.cmds as mc
import maya.OpenMaya as om

def retSel():
  return mc.ls(sl=1)

def attachToMotionpath(obj, crv, crv_param, obj_up):
  obj = obj
  crv = crv
  crv_param = crv_param/8.0
  obj_up = obj_up
  
  if obj_up:
    mpath = mc.pathAnimation(
    obj,
    c=crv,
    fractionMode = True,
    follow = True,
    followAxis = "x",
    upAxis = "y",
    worldUpType = "object",
    worldUpObject = obj_up, 
    inverseUp = False, 
    inverseFront = False,
    bank = False,
    startTimeU = 1,
    endTimeU = 1
    )
  else:
    mpath = mc.pathAnimation(
    obj,
    c=crv,
    fractionMode = True,
    follow = True,
    followAxis = "x",
    upAxis = "y",
    worldUpType = "scene", 
    inverseUp = False, 
    inverseFront = False,
    bank = False,
    startTimeU = 1,
    endTimeU = 1
    )
  
  
  #break the motions path's time values and set to crv_param  
  mc.delete(mpath+"_uValue")
  tmp_value = (mpath+".uValue")
  mc.setAttr(tmp_value, crv_param)

def closestPointOnCurve(object, curveObject):
  location = mc.xform(object, q=1, ws=1, sp=1)
  
  curve = curveObject
        
        # put curve into the MObject
  tempList = om.MSelectionList()
  tempList.add(curve)
  curveObj = om.MObject()
  tempList.getDependNode(0, curveObj)  # puts the 0 index of tempList's depend node into curveObj
        
        # get the dagpath of the object
  dagpath = om.MDagPath()
  tempList.getDagPath(0, dagpath)
        
        # define the curve object as type MFnNurbsCurve
  curveMF = om.MFnNurbsCurve(dagpath)
        
        # what's the input point (in world)
  point = om.MPoint( location[0], location[1], location[2])
        
        # define the parameter as a double * (pointer)
  prm = om.MScriptUtil()
  pointer = prm.asDoublePtr()
  om.MScriptUtil.setDouble (pointer, 0.0)
        
  # set tolerance
  tolerance = .00000001
        
  # set the object space
  space = om.MSpace.kObject
        
  # result will be the worldspace point
  result = om.MPoint()
  result = curveMF.closestPoint (point, pointer,  0.0, space)
        
  position = [(result.x), (result.y), (result.z)]
  curvePoint = om.MPoint ((result.x), (result.y), (result.z))
        
  parameter = om.MScriptUtil.getDouble (pointer)
        
  # just return - parameter, then world space coord.
  return parameter


def main():
  sel = mc.ls(sl=1)
  
  objects = sel[0:(len(sel)-1)]
  crv = sel[-1]
  
  crv_up = mc.duplicate(crv)
  crv_up = str(crv_up[0])
  
  set_vis = crv_up+".visibility"
  mc.setAttr(set_vis, 0)
  
  for obj in objects:
    #get position of objs
    x = mc.getAttr((obj+".tx"))
    y = mc.getAttr((obj+".ty"))
    z = mc.getAttr((obj+".tz"))
    
    #make locator at obj position
    loc=mc.spaceLocator (p=(x, y, z))
    loc = str(loc[0])
    
    #store parameter
    crv_param =closestPointOnCurve(obj, crv)
    print "crv_param: %d" %crv_param
    
    #attach to obj_up to duplicate crv
    attachToMotionpath(loc, crv_up, crv_param, False)
    
    #attach to obj to original crv
    attachToMotionpath(obj, crv, crv_param, loc)
    
    set_vis = loc+".visibility"
    mc.setAttr(set_vis, 0)
  
  mc.move(0, 1, 0, crv_up)
  
   

  
if __name__ == '__main__':
    main()
main()


