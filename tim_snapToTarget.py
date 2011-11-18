#!/usr/bin/env python
# encoding: utf-8
"""
tim_snapToTarget.py

Created by Tim Reischmann on 2011-05-23.
Copyright (c) 2011 Tim Reischmann. All rights reserved.
"""

from pymel.core import *
#from tim_locatorAtTarget import make_loc
import tim_locatorAtTarget

def snap_to_target():
  sel = ls(sl=1, flatten=1)
  
  if len(sel):
    target_str = str(sel[0])
    target = tim_locatorAtTarget.make_loc(target_str)
    
    target_pos = xform(target, scalePivot=1, query=1, worldSpace=1)
    target_rot = xform(target, rotation=1, query=1, worldSpace=1)
    
    xform(sel[1], translation = (target_pos[0], target_pos[1], target_pos[2]), worldSpace=1)
    xform(sel[1], rotation = (target_rot[0], target_rot[1], target_rot[2]), worldSpace=1)
    
    delete(target)
  else: warning("##snap_to_target: Select the target, then the obj to snap")
  
  
#LTB:import tim_snapToTarget;reload(tim_snapToTarget);tim_snapToTarget.snap_to_target()
