#LTB: import tim_cleanTwoCurves;reload(tim_cleanTwoCurves);tim_cleanTwoCurves.main()
from pymel.core import *

def main():
  sel_crvs = keyframe(q=1, n=1)
  #nodeType(sel_crvs[0])
  many_keys = keyframe(sel_crvs[1], q=1)
  few_keys = keyframe(sel_crvs[0], q=1)
  
  for key in many_keys:
      if not key in few_keys:
          selectKey(sel_crvs[1], t=(key,key), r=1)
          cutKey(clear=1);
  


'''
from pymel.core import *

range(len(keyframe(q=1, n=1)))

i=0

for i in range(len(keyframe(q=1, n=1))) 
  sel_crvs = keyframe(q=1, n=1)
  #nodeType(sel_crvs[0])
  many_keys = keyframe(sel_crvs[1], q=1)
  few_keys = keyframe(sel_crvs[0], q=1)
  
  for key in many_keys:
      if not key in few_keys:
          selectKey(sel_crvs[1], t=(key,key), r=1)
          cutKey(clear=1);
  
  i+=2
'''
