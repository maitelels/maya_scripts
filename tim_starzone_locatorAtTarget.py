#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_starzone_locatorAtTarget;reload(tim_starzone_locatorAtTarget);tim_starzone_locatorAtTarget.make_loc()
"""
tim_starzone_locatorAtTarget.py

Created by Tim Reischmann on 2011-05-12.
Copyright (c) 2011 Tim Reischmann. All rights reserved.
"""


from pymel.core import *

proc_name = "## tim_starzone_locatorAtTarget: " 

def replace_all_characters(text, dic={':':'_', }):
  '''
  This function will replace all occurrences
  of a character will another one.
  
  Needs a dictionary in the form of {'original':'replacement',}
  '''
  for i, j in dic.iteritems():
      text = text.replace(i, j)
  return text


def build_loc(sel):
  '''
  This function will build a locator.
  Snap it to the target position.
  Delete the constraints afterwards.
  
  Needs a string 
  '''
  if objExists(sel):
    try:
      # build the name and the locator
      loc_name = (replace_all_characters(sel)+"_loc")
      loc = spaceLocator (name = loc_name)
      
      # snap it to the desired position using constraints
      p_con = pointConstraint(sel, loc)
      o_con = orientConstraint(sel, loc)
      s_con = scaleConstraint(sel, loc)
      
      #cleanup
      delete(p_con, o_con, s_con)
      parentConstraint(loc, sel)
      print "%s Created '%s'" % (proc_name, loc_name)
      
      return loc_name
    except:
      print "%s Could not create '%s'" % (proc_name, loc_name);
  else:
    print "%s Error: '%s' does not exist" % (proc_name, sel)

def make_loc(sel=0):
  '''tim_starzone_locatorAtTarget
  
  Will build a locator for every obj it gets passed.
  Locator will be build in the objs location.
  
  Takes a
  - selection from within Maya
  - list of objs
  - string   
  '''
  all_locs = []
  # check if passed type is Maya selection
  if sel == 0:
    sel = ls(sl=1)
    if sel:
      for s in sel:
        all_locs.append(build_loc(s))
      return all_locs
    else: error("%s Nothing Selected"% proc_name) 
  
  # check if passed type is a string
  if isinstance(sel, str):
    if sel:
      all_locs.append(build_loc(sel))
      return all_locs
  
  # check if passed type is a list
  if isinstance(sel, list):
    if sel:
      for s in sel:
        all_locs.append(build_loc(s))
      return all_locs
      

