#LTB: import tim_bakeJitter;reload(tim_bakeJitter);tim_bakeJitter.random()
import pymel.core as pm    
import random

"""
Offset current translate values by 1 in either direction
"""
def random():
  sel = pm.selected()
  
  animStartTime = pm.playbackOptions(animationStartTime=1, q=1)
  animEndTime = pm.playbackOptions(animationEndTime=1, q=1)
  
  
  
  while animStartTime<=animEndTime:
    for s in sel:
        s.translateX.set(s.translateX.get()+random.uniform(-.1,.1))
        s.translateY.set(s.translateY.get()+random.uniform(-.1,.1))
        s.translateZ.set(s.translateZ.get()+random.uniform(-.1,.1))
    pm.setKeyframe(attribute="translate", time=animStartTime)
    animStartTime+=1

    
"""
Add random rotation over a period of time using the startvalue
"""
def fixedSeed():
  sel = pm.selected()
  
  animStartTime = pm.playbackOptions(animationStartTime=1, q=1)
  animEndTime = pm.playbackOptions(animationEndTime=1, q=1)
    
  for attr in sel:
    animStartTime = pm.playbackOptions(animationStartTime=1, q=1)
    animEndTime = pm.playbackOptions(animationEndTime=1, q=1)
    
    xVal = attr.rotateX.get()
    yVal = attr.rotateY.get()
    zVal = attr.rotateZ.get()
  
    print animStartTime
    print animEndTime
    print xVal
    print yVal
    print zVal
      
    while animStartTime<=animEndTime:
      attr.rotateX.set(xVal+random.uniform(-.1,.1))
      attr.rotateY.set(yVal+random.uniform(-.1,.1))
      attr.rotateZ.set(zVal+random.uniform(-.1,.1))
      pm.setKeyframe(attribute="rotate", time=animStartTime)
      animStartTime+=1
    

