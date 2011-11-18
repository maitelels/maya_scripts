#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_versionUpCam;reload(tim_versionUpCam);tim_versionUpCam.main()

"""
tim_versionUpCam.py

Created by Tim Reischmann on 2011-10-27.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

usage:
import tim_versionUpCam;reload(tim_versionUpCam);tim_versionUpCam.main()

"""


import pymel.core as pm
from datetime import datetime
import re

#Global Var definitions
proc_name = '## tim_versionUpCam: '

def main():
	prefRun()
	
	for s in pm.selected():
		old_name = s.name()
		new_name = cameraUp(old_name)
		pm.rename(old_name, new_name)
		print old_name, "->", new_name
	
	
def cameraUp(name):
	pattern = "_"
	old_version = ""
	new_version = ""
	
	name_parts = re.split(pattern, name)
	
	for name_part in name_parts:
		if name_part[0] == "v":
			
			old_version = name_part
			new_version = versionUp(old_version)
	
	new_name = name.replace(old_version, new_version)
	
	return new_name

def versionUp(version):
    digits = len(version[1:])
    version_number = int(version[1:])
    version_number += 1
    
    str_version_number = r"v%0"+str(digits)+"d"
    return str_version_number % version_number	

def prefRun():
	'''prefix script run with script name und datetime
	'''
	print '\n\n\n',proc_name,
	print datetime.now(),'##'

