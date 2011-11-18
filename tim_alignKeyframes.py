#LTB: import tim_alignKeyframes;reload(tim_alignKeyframes);

from pymel.core import *

def align(to='last'):
  if to=='last' or to == 'minimum' or to == 'maximum':
    
    value = 0.0
    #get all keyframe values from selection
    keys = keyframe(q=1, valueChange=1)
    
    #check wether to min, max keyframes or use last selected
    if to == 'last':
      value = keyframe(q=1, lsl=1, valueChange=1)[0]
     
    else:
      if to == 'minimum':
        value = min(keys)
      if to == 'maximum':
        value = max(keys)
    
    
    #change selected keyframes accordingly
    keyframe(e=1, valueChange=value)
 
  else:
    print("ERROR: call script with either 'minimum', 'maximum' or no parameter") 