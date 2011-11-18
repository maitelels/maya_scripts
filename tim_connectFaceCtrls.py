from pymel.core import *

def connectFaceCtrls(source_char, target_char):
  print "Source Character: %s" % source_char
  print "Target Character: %s" % target_char
  
  mouth_to_connect = ('jaw_open',
                      'jaw_side',
                      'jaw_forBack',
                      'lips_close',
                      'lips_sticky',
                      'lip_close_mid',
                      'wideNarrow_L',
                      'wideNarrow_R',
                      'mouth_upDown',
                      'mouth_leftRight',
                      'upLip_roll',
                      'lowLip_roll',
                      'upLip_inOut',
                      'lowLip_inOut',
                      'lipCorner_upDown_L',
                      'lipCorner_upDown_R',
                      'upLip_upDown_L',
                      'upLip_upDown_R',
                      'lowLip_upDown_L',
                      'lowLip_upDown_R',
                      'lipCorner_tight_L',
                      'lipCorner_tight_R',
                      'upLip_upDown_M',
                      'lowLip_upDown_M',
                      'noseSnear_L',
                      'noseSnear_R',
                      'noseTip_upDown',
                      'noseTip_side',
                      'nose_puff_L',
                      'nose_puff_R',
                      'cheek_puff_L',
                      'cheek_puff_R',
                      'chin_upDown',
                      'chin_side',
                      'chin_tight')
                      
  eyes_to_connect =  ('upLid_openClose_L',
                      'upLid_openClose_R',
                      'lowLid_openClose_L',
                      'lowLid_openClose_R',
                      'upLid_shape_L',
                      'upLid_shape_R',
                      'lowLid_shape_L',
                      'lowLid_shape_R',
                      'lid_line_L',
                      'lid_line_R',
                      'lids_cornea',
                      'lids_auto',
                      'squint_inner_L',
                      'squint_inner_R',
                      'squint_outer_L',
                      'squint_outer_R',
                      'brow_squeeze_L',
                      'brow_squeeze_R',
                      'browInner_upDown_L',
                      'browInner_upDown_R',
                      'browMid_upDown_L',
                      'browMid_upDown_R',
                      'browOut_upDown_L',
                      'browOut_upDown_R',
                      'ear_bendMid_L',
                      'ear_bendUp_L',
                      'ear_rollMid_L',
                      'ear_rollUp_L',
                      'ear_bendMid_R',
                      'ear_bendUp_R',
                      'ear_rollMid_R',
                      'ear_rollUp_R',
                      'eyeCorners_tight_in_L',
                      'eyeCorners_tight_out_L',
                      'eyeCorners_tight_in_R',
                      'eyeCorners_tight_out_R')
  
  for attr in mouth_to_connect:
    sourceAttr = source_char+":"+"faceCtrl_mouth."+attr
    targetAttr = target_char+":"+"faceCtrl_mouth."+attr
    
    try:
      connectAttr(sourceAttr, targetAttr, f=1)
    except:
      print "ERROR: Can't connect %s to %s" % (sourceAttr, targetAttr)
      
  for attr in eyes_to_connect:
    sourceAttr = source_char+":"+"faceCtrl_eyes."+attr
    targetAttr = target_char+":"+"faceCtrl_eyes."+attr
    
    try:
      connectAttr(sourceAttr, targetAttr, f=1)
    except:
      print "ERROR: %s cannot be connected to %s" % (sourceAttr, targetAttr) 
    
  
  
  
  
def main():
  connectFaceCtrls("KB", "FB")
  
main()
