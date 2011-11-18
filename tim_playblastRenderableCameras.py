#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_playblastRenderableCameras;reload(tim_playblastRenderableCameras);tim_playblastRenderableCameras.main()

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
	prefRun()
	#get all renderable cameras in scene
	allCamShapes = pm.ls( type='camera')

	
	cams = []
	for cam in allCamShapes:
		if pm.getAttr(cam+".renderable"):
			cams.append(pm.listRelatives(cam, p=1))
			
	print cams
		
	
	#Get the current frame range from the timeslider
	startTime = pm.playbackOptions(q=True, min=True )
	endTime = pm.playbackOptions(q=True, max=True )
	
	print "Playblasting Cameras:",
	
	#generate playblast for each renderable cam
	for cam in cams:
		pm.playblast(
			cam, 
			startTime=startTime, 
			endTime=endTime, 
			viewer=0, 
			#filename="X:/Projects/GREY11_ANM71_Rewe_Starzone/GR11A71_Shots/GR11A71_Animatic/Animatic_Maya/data/test"+cam[0])
			)
	
	print "for range: %04d - %04d" % (startTime,endTime)

		
def prefRun():
	'''prefix script run with script name und datetime
	'''
	print '\n\n\n',proc_name,
	print datetime.now(),'##'

