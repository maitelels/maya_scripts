# create a new shader
import pymel.core as pm

def createShader(shaderType='lambert', name=''):
  shdr, sg = pm.createSurfaceShader(shaderType, name
  
  return shdr, sg


def createFileTexture():
  pass

def connectFileTextureToVRayMtl():
  pass

def connectVRayMtlToVRayMtl2Sided():
  pass
  



def assignShader(shadingGroup=None, objects=None):
  # assign selection to the shader
  print "###########"
  if objects is None:
    objects = pm.ls(sl=True, l=True)
    for obj in objects:
      try:
        print obj, 
        pm.sets(i, e=True, forceElement=shadingGroup)
      except:
        pass

'''
Example:
# run the next line
shader, shaderSG = createShader('blinn', 'foobar')
# SELECT SOME OBJECTS
# run the next line to assign the selected object to the shader
assignToShader(shaderSG)
'''