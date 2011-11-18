#LTB: import tim_randLinguine;reload(tim_randLinguine);tim_randLinguine.main() 

from pymel.core import *
import random

sel = selected()
for s in sel:
    #flip random axis
    s.rotateY.set(random.choice([random.uniform(-10.0, 10.0), random.uniform(170.0, 190.0)]))
    s.rotateX.set(random.choice([random.uniform(-.5, .5), random.uniform(179.5, 180.5)]))
    s.rotateZ.set(random.choice([random.uniform(-.5, .5), random.uniform(179.5, 180.5)]))
    s.translateY.set(s.translateY.get()+random.uniform(-.1,.1))
