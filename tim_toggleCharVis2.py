from pymel.core import *

def setCharVis(char, bodyLo, headLo, bodyHi, headHi):
  
  setAttr((char+":lowres_R_leg.visibility"), bodyLo)
  setAttr((char+":lowres_L_leg.visibility"), bodyLo)
  setAttr((char+":lowres_R_arm.visibility"), bodyLo)
  setAttr((char+":lowres_L_arm.visibility"), bodyLo)
  setAttr((char+":lowres_body.visibility"), bodyLo)
  setAttr((char+":lowres_head.visibility"), headLo)
  setAttr((char+":fullDeformation.visibility"), bodyHi)
  setAttr((char+":fullDeformation_head.visibility"), headHi)
  print "%s | bodyLo:%i | headLo:%i | bodyHi:%i | headHi:%i" % (char, bodyHi, bodyLo, headHi, headLo)
  
def toggleCharVis2(char):
  bodyLo = getAttr(char+":lowres_body.visibility")
  headLo = getAttr(char+":lowres_head.visibility")
  bodyHi = getAttr(char+":fullDeformation.visibility")
  headHi = getAttr(char+":fullDeformation_head.visibility")
  
  if bodyLo==0 and headLo==0 and bodyHi==0 and headHi==0:
    setCharVis(char, bodyLo=1, headLo=1, bodyHi=0, headHi=0)
  
  elif bodyLo==1 and headLo==1 and bodyHi==0 and headHi==0:
    setCharVis(char, bodyLo=1, headLo=0, bodyHi=0, headHi=1)
  
  elif bodyLo==1 and headLo==0 and bodyHi==0 and headHi==1:
    setCharVis(char, bodyLo=0, headLo=0, bodyHi=1, headHi=1)
  
  elif bodyLo==0 and headLo==0 and bodyHi==1 and headHi==1:
    setCharVis(char, bodyLo=0, headLo=0, bodyHi=0, headHi=1)
  
  elif bodyLo==0 and headLo==0 and bodyHi==0 and headHi==1:
    setCharVis(char, bodyLo=1, headLo=1, bodyHi=0, headHi=0)
