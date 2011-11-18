#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_newMaterial;reload(tim_newMaterial);tim_newMaterial.main()

"""
tim_newMaterial.py

Created by Tim Reischmann on 2011-10-27.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

usage:
import tim_newMaterial;reload(tim_newMaterial);tim_newMaterial.main()

"""


import pymel.core as pm
from datetime import datetime
import re, os

#Global Var definitions
proc_name = '## tim_newMaterial: '

def main():
  prefRun()
  
  textures = getTextureNames()
  pages = pm.ls("page*_paper_geo")
  #pages = pages[:-1]

  textureIndex = 0
  
  for page in pages:
    print "##"
    currentPage =  pm.ls(page)
    
    texture1 = textures[textureIndex]
    textureIndex +=1
    
    useVRayMtl(currentPage, texture1)
    print texture1
    
    even_odd = 0
     
      

def useVRayMtl(currentPage, texture1):
  shdr, sg = pm.createSurfaceShader( 'VRayMtl', currentPage[0]+"_shdr" )
  pm.sets( sg, forceElement=currentPage )
  filenode = pm.createNode('file', name=currentPage[0]+"_file")
  filenode.fileTextureName.set(texture1)
  pm.connectAttr( filenode+".outColor", shdr.color , force=1)
  placement = pm.shadingNode('place2dTexture', asUtility=1, name='placeTextureName')
  
  pm.connectAttr(placement.outUV, filenode.uvCoord, f=1) 
  pm.connectAttr(placement.outUvFilterSize, filenode.uvFilterSize, f=1) 
  pm.connectAttr(placement.coverage, filenode.coverage, f=1) 
  pm.connectAttr(placement.translateFrame, filenode.translateFrame, f=1) 
  pm.connectAttr(placement.rotateFrame, filenode.rotateFrame, f=1) 
  pm.connectAttr(placement.mirrorU, filenode.mirrorU, f=1) 
  pm.connectAttr(placement.mirrorV, filenode.mirrorV, f=1) 
  pm.connectAttr(placement.stagger, filenode.stagger, f=1) 
  pm.connectAttr(placement.wrapU, filenode.wrapU, f=1) 
  pm.connectAttr(placement.wrapV, filenode.wrapV, f=1) 
  pm.connectAttr(placement.repeatUV, filenode.repeatUV, f=1) 
  pm.connectAttr(placement.vertexUvOne, filenode.vertexUvOne, f=1) 
  pm.connectAttr(placement.vertexUvTwo, filenode.vertexUvTwo, f=1) 
  pm.connectAttr(placement.vertexUvThree, filenode.vertexUvThree, f=1) 
  pm.connectAttr(placement.vertexCameraOne, filenode.vertexCameraOne, f=1) 
  pm.connectAttr(placement.noiseUV, filenode.noiseUV, f=1) 
  pm.connectAttr(placement.offset, filenode.offset, f=1) 
  pm.connectAttr(placement.rotateUV, filenode.rotateUV, f=1)
  pm.setAttr(placement.rotateFrame, 90)
  pm.setAttr(placement.repeatU, -1)

def useVRayMtl2Sided(texture):
  pass


def prefRun():
  '''prefix script run with script name und datetime'''
  print '\n\n\n',proc_name,
  print datetime.now(),'##'
  
def getTextureNames():
  textures = []
  for i in range(52):
    directoryName = r"X:\Projects\GREY11_ANM71_Rewe_Starzone\GR11A71_3D\GR11A71_Textures\Album\Seiten_tim".replace("\\", "/")
    fileName = "/albumseite.%03i.jpg" % (i+1)
    textures.append(directoryName+fileName)
    #textures.append(fileName)
  return textures
