#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_loadAndAssignTexturesToObjects;reload(tim_loadAndAssignTexturesToObjects);tim_loadAndAssignTexturesToObjects.main()

"""
tim_playblastRenderableCameras.py

Created by Tim Reischmann on 2011-10-27.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

usage:
import tim_playblastRenderableCameras;reload(tim_playblastRenderableCameras);tim_playblastRenderableCameras.main()

"""


import pymel.core as pm
from datetime import datetime

#Global Var definitions
proc_name = '## tim_playblastRenderableCameras: '

def main():
	pass


def prefRun():
	'''prefix script run with script name und datetime
	'''
	print '\n\n\n',proc_name,
	print datetime.now(),'##'

main()



'''
import maya.cmds as mc
#create a new shader
def createShader(shaderType='lambert', name=''):
if name == '':
name = shaderType
name = mc.shadingNode(shaderType, asShader=True,  name=name)
sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='%sSG'
%(name))

# connect shader to SG
shaderOutput = 'outValue'
if shaderType== 'mia_material' or shaderType == 'mia_material_x':
if shaderType == 'mia_material_x':
shaderOutput = "result";
mc.connectAttr('%s.%s' %(name,shaderOutput), '%s.miMaterialShader' %(sg),
force=True)
mc.connectAttr('%s.%s' %(name,shaderOutput), '%s.miShadowShader' %(sg),
force=True)
mc.connectAttr('%s.%s' %(name,shaderOutput), '%s.miPhotonShader' %(sg),
force=True)
else:
mc.connectAttr('%s.outColor' %(name), '%s.surfaceShader' %(sg), force=True)
 return [name, sg]

def assignToShader(shaderSG=None, objects=None):
# assign selection to the shader
if objects is None:
objects = mc.ls(sl=True, l=True)
for i in objects:
print i
try:
mc.sets(i, e=True, forceElement=shaderSG)
except:
pass
'''



"""
Example:
# run the next line
shader, shaderSG = createShader('blinn', 'foobar')
# SELECT SOME OBJECTS
# run the next line to assign the selected object to the shader
assignToShader(shaderSG)
"""

'''

import maya.cmds as mc
#create a new shader
def createShader(shaderType='lambert', name=''):
    if name == '':
        name = shaderType
        name = mc.shadingNode(shaderType, asShader=True,  name=name)
        sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='%sSG' %(name))
    
        # connect shader to SG
        shaderOutput = 'outValue'
        mc.connectAttr('%s.outColor' %(name), '%s.surfaceShader' %(sg), force=True)
        return [name, sg]

def assignToShader(shaderSG=None, objects=None):
    # assign selection to the shader
    if objects is None:
        objects = mc.ls(sl=True, l=True)
        for i in objects:
            print i
    try:
        mc.sets(i, e=True, forceElement=shaderSG)
    except:
        pass
        
#########

shader, shaderSG = createShader('blinn', 'foobar')
assignToShader(shaderSG)

'''
