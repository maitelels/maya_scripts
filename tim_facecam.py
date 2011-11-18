from pymel.core import *

def facecam(char):
  char = char
  
  sel = ls(sl=1)
  select(cl=1)
  
  # attach a facecam to the characters head ctrl
  facecam = camera(nearClipPlane=0.01, farClipPlane=10000, focalLength=55, name=(char+"_facecam"))
  select(facecam, r=1)
  facecam_grp = group(name=(facecam[0]+"_grp"))
  target_handle = char + ":hdl_head"
  xform(facecam, translation=(0, 1.5, 18))
  xform(facecam, pivots=(0,0,0), ws=1)
  facecam_constaint = parentConstraint(target_handle, facecam_grp)
  
  # lock and hide the new camera grp 
  setAttr((facecam[0]+".tx"), lock=1);
  setAttr((facecam[0]+".ty"), lock=1);
  setAttr((facecam[0]+".tz"), lock=1);
  setAttr((facecam_grp+".visibility"), 0);
  
  #restore initial selection
  select(sel, r=1)

def make_facecam():
  if ls(sl=1):
    # get namespace and check wether or not it is a valid character
    char = ls(sl=1)[0].split(":")[0]
    if char == "KB" or char == "FB":
      facecam(char)
    
    # throw error if selection is not a valid character
    else: error("Select a Character Controller!")
  else: error("Select S O M E T H I N G !")
