#LTB:import tim_LTB2;reload(tim_LTB2);tim_LTB2.main()

"""
NAME: Little Toolbox 2
VERSION: 2.0
FILE: tim_LTB2.py

Created by Tim Reischmann on 2011-06-09.
Copyright (c) 2011 Tim Reischmann. All rights reserved.
"""

#pymel for Maya cmds
#os for path manipulation
#re for finding script call in files
from pymel.core import *
import os, re


def printl(list):
  '''## LTB2 ##
  SCRIPT: printl
  
  print a list one line per item
  '''
  for l in list:
    print l

    
def printd(dictionary):
  '''## LTB2 ##
  SCRIPT: printd
  
  print a dictionary one line per key
  '''
  for script in dictionary:
    print "\n",script['name'].upper()
    for k,v in script.iteritems():
      print "%s: %s" % (k,v)

      
def prepare_list(scripttype, directory):
  '''## LTB2 ##
  SCRIPT: prepare_list(scripttype, directory)
  
  ARGUMENTS:
  scripttype can be ".mel" or ".py"
  directory is ideally a raw string
  
  USE:
  - in a given directory
  - check for files
  - of type .mel or .py
  - return a list of dictionaries with file info
  '''
  dir_name = directory
  file_list = [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
  mel_scripts = []
  py_scripts = []
    
  for file_name in file_list:
    if re.search(r'.mel$', file_name):
      mel_scripts.append(LTB_builddict(file_name, dir_name))
    if re.search(r'.py$', file_name):
      py_scripts.append(LTB_builddict(file_name, dir_name))

  if scripttype == "mel":
    return mel_scripts
  
  if scripttype == "py":
    return py_scripts

    
def get_command_from_file(fullname, identifier):
  '''## LTB2 ##
  SCRIPT: get_command_from_file(fullname, identifier)
  
  ARGUMENTS:
  identifier could be
  r"//LTB:.+"  for .mel or
  r"#LTB:.+"   for .py
  but any other search string will work.
  
  fullname is a complete filenaem with path and extension, e.g.
  r"C:\Users\User\Documents\maya\scripts\foo.py"
  
  USE:
  - for a given file
  - return the contents of a line
  - starting with a certain identifier
  '''
  f = open(fullname, 'r')
  text = f.read()
  f.close()
  LTB_command = re.search(identifier, text)
  LTB_command = LTB_command.group(0).split(':',1)
  return LTB_command[1].lstrip().rstrip()
 

def LTB_builddict(file_name, dir_name):
  '''## LTB2 ##
  SCRIPT: LTB_builddict(file_name, dir_name)
  
  ARGUMENTS:
  file_name is filename and extension, e.g.
  foo.py
  
  dir_name is an absolut path, e.g.
  r"C:\Users\Farmer\Documents\maya\scripts\"
  
  USE:
  - build a dictionary for a given file
  - containing
  name: foo
  fullname: C:\\Users\\Farmer\\Documents\\maya\\scripts\\foo.py 
  path: C:\\Users\\Farmer\\Documents\\maya\\scripts\\
  ext: .py
  prep: 1 
  com: import foo;reload(foo);foo.main()
  '''
  (shortname, extension) = os.path.splitext(file_name)
  identifier = None
  fullpath = os.path.join(dir_name,file_name)
  ready = None
  command = None
 
  if extension == ".mel":
    identifier = r"//LTB:.+"
  elif extension == ".py":
    identifier = r"#LTB:.+"

  try:
    command = get_command_from_file(fullpath, identifier)
    ready=1
  except:
    ready=0
 
  ltb_dict = dict(name=shortname,
                  fullname=fullpath,
                  path=dir_name,
                  ext=extension,
                  prep=ready,
                  com = command,
                  )
  return ltb_dict

def strip_tim(string):
  '''## LTB2 ##
  SCRIPT: strip_tim(string)
  
  check if string start with tim_ and return it without
  '''
  if "tim_" in string:
    ret_val = string.split("_", 1)[1]
    return ret_val
  elif "tnr" in string:
    ret_val = string[3:]
    return ret_val
  else:
    return string

def add_mel_cmd(string):
  '''## LTB2 ##
  SCRIPT: add_mel_cmd(string)
  
  mel command needs to be encapsulated in a 
  python call in order for it to execute.
  '''
  pre = r"import maya.mel as mel;mel.eval('"
  post = r"')" 
  return ("%s%s%s") % (pre,string,post)
  
def LTB_show(all_scripts):
  
  
  if window('LTB2_window', q=True, ex=True):
    deleteUI('LTB2_window')
  
  
  LTB_UI = window('LTB2_window', title="Little Tool Box 2", iconName='LTB2', width=280)
  LTB_layout = columnLayout()
  
  
  print "\n## LTB2 loaded: ##"
  
  for scr in all_scripts:
    if scr['ext'] == '.mel':
      scr['com'] = add_mel_cmd(scr['com'])
    
      
    if scr['prep'] == 1:
      scr['name'] = strip_tim(scr['name'])
      button(width=280,label=scr['name'], command=scr['com'])
      print "SCRIPT: %s | COMMAND: %s" % (scr['name'],scr['com'])
  
  showWindow(LTB_UI)
  
  
def main(scripttype='py', 
         directory = r"C:\Users\tReischmann\Documents\maya\scripts"):
  
  if scripttype == 'mel':
    mel = prepare_list('mel', directory)
    LTB_show(mel)
  
  if scripttype == 'py':
    py = prepare_list('py', directory)
    LTB_show(py)

  return  "LTB2: loaded '%s' scripts from %s" % (scripttype, directory)
 
if __name__ == "__main__":
  main()


