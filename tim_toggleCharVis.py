from pymel.core import *

def build_attr_names(char):
  return ((char+":lowres_R_leg.visibility"),
          (char+":lowres_L_leg.visibility"),
          (char+":lowres_R_arm.visibility"),
          (char+":lowres_L_arm.visibility"),
          (char+":lowres_head.visibility"),
          (char+":lowres_body.visibility"),
          (char+":fullDeformation.visibility"),
          (char+":fullDeformation_head.visibility"))  

def toggleCharVis(char):
  r_leg, l_leg, r_arm, l_arm, head, body, deform, deform_head = build_attr_names(char)
  
  #if BODY: off, HEAD: off
  if (getAttr(deform) == 0 and
      getAttr(deform_head) == 0 and 
      getAttr(body) == 0):
    setAttr(r_leg, 1)
    setAttr(l_leg, 1)
    setAttr(r_arm, 1)
    setAttr(l_arm, 1)
    setAttr(body, 1)
    setAttr(head, 1)
    setAttr(deform, 0)
    setAttr(deform_head, 0)
    print "%s|BODY: low, HEAD: low" % char
  
  #if BODY: low, HEAD: low
  elif (getAttr(deform) == 0 and 
      getAttr(deform_head) == 0 and 
      getAttr(body) == 1):
    setAttr(r_leg, 1)
    setAttr(l_leg, 1)
    setAttr(r_arm, 1)
    setAttr(l_arm, 1)
    setAttr(body, 1)
    setAttr(head, 0)
    setAttr(deform, 0)
    setAttr(deform_head, 1)
    print "%s|BODY: low, HEAD: high" % char
  
  #if BODY: low, HEAD: high
  elif (getAttr(deform) == 0 and 
      getAttr(deform_head) == 1 and
      getAttr(body) == 1):
    setAttr(r_leg, 0)
    setAttr(l_leg, 0)
    setAttr(r_arm, 0)
    setAttr(l_arm, 0)
    setAttr(body, 0)
    setAttr(head, 0)
    setAttr(deform, 1)
    setAttr(deform_head, 1)
    print "%s|BODY: high, HEAD: high" % char
  
  #if BODY: high, HEAD: high
  elif (getAttr(deform) == 1 and 
      getAttr(deform_head) == 1 and
      getAttr(body) == 0):
    setAttr(r_leg, 0)
    setAttr(l_leg, 0)
    setAttr(r_arm, 0)
    setAttr(l_arm, 0)
    setAttr(body, 0)
    setAttr(head, 0)
    setAttr(deform, 0)
    setAttr(deform_head, 1)
    print "%s|BODY: off, HEAD: high" % char
    
  #if BODY: off, HEAD: high
  elif (getAttr(deform) == 0 and 
      getAttr(deform_head) == 1 and
      getAttr(body) == 0):
    setAttr(r_leg, 0)
    setAttr(l_leg, 0)
    setAttr(r_arm, 0)
    setAttr(l_arm, 0)
    setAttr(body, 0)
    setAttr(head, 0)
    setAttr(deform, 0)
    setAttr(deform_head, 0)
    print "%s|BODY: off, HEAD: off" % char
