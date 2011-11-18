#LTB: import tim_cleanUpRetiming;reload(tim_cleanUpRetiming)

#!/usr/bin/python

import maya.cmds as mc

'''
get names of all curves attached to selection and store them in a list
'''
objects = mc.ls(sl = 1)
object_curves = []
for object in objects:
  crv = mc.listConnections(object, type = 'animCurve')
  if crv is not None:
    object_curves.extend(crv)


'''
look for keyframes not on a full frame and clean them up,
by rounding keyframe values up and down and creating new
keyframes at the respective position and then deleting
the original keyframe.
'''
for crv in object_curves:
  keyframes = mc.keyframe(crv, q=1)
  #print crv
 
  for keyframe in keyframes:
    keyframe_base = float(int(keyframe))
    keyframe_offset = keyframe%keyframe_base
    
    if keyframe_offset != 0.0:
      attr = mc.listConnections(crv, plugs=1)
      attr = str(attr[0]).split(".")
     
      
      print '##########'
      print "attr", attr
      print "keyframe", keyframe
      print "keyframe_base", keyframe_base
      print "keyframe_offset", keyframe_offset
      print "attr", attr
      print "attr[0]", attr[0]
      print "attr[1]", attr[1]
      
     
      old_keyframe = mc.keyTangent(attr[0],
                                   q=True,
                                   time=(keyframe,),
                                   attribute=attr[1],
                                   inAngle=1,
                                   inWeight=1,
                                   outAngle=1,
                                   outWeight=1,
                                   inTangentType=1,
                                   outTangentType=1 )
     
      '''
      print '##########'
      print object_attr[0]
      print attr[1]
      print ''
      #print (keyframe_base+round_up)
      print ''
      print old_keyframe[0]
      print old_keyframe[1]
      print old_keyframe[2]
      print old_keyframe[3]
      print old_keyframe[4]
      print old_keyframe[5]
      '''
     
      round_up = 0
      if keyframe >= (keyframe_base+0.5):
        round_up += 1
        #print "aufrunden"
       
      mc.setKeyframe(crv, time=(keyframe_base+round_up), insert=1)
     
     
      mc.keyTangent(attr[0],
                    e=True,
                    time=((keyframe_base+round_up),),
                    attribute=attr[1],
                    absolute=1,
                    inAngle=old_keyframe[0],
                    outAngle=old_keyframe[1],
                    inWeight=old_keyframe[2],
                    outWeight=old_keyframe[3] )
     
      mc.keyTangent(attr[0],
                    e=True,
                    time=((keyframe_base+round_up),),
                    attribute=attr[1],
                    inTangentType=old_keyframe[4],
                    outTangentType=old_keyframe[5] )
     
     
      mc.selectKey(crv, replace=1, keyframe=1, time=(keyframe, ))
      mc.cutKey(animation='keys', clear=1)
 


'''
import tim_cleanUpRetiming
reload(tim_cleanUpRetiming)
import sys
sys.path.insert(0, "/hosts/garlinge/user_data/RND/myScripts/constraintManager/trunk/constraintManager")
'''
