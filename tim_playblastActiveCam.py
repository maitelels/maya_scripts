#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_playblastActiveCam;reload(tim_playblastActiveCam);tim_playblastActiveCam.main()

"""
tim_playblastActiveCam.py

Created by Tim Reischmann on 2011-10-27.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

usage:
import tim_playblastActiveCam;reload(tim_playblastActiveCam);tim_playblastActiveCam.main()

"""


import pymel.core as pm
from datetime import datetime

#Global Var definitions
proc_name = '## tim_playblastActiveCam: '

def main():
	prefRun()
	
	renderWidth = pm.getAttr("defaultResolution.width")
	renderHeight = pm.getAttr("defaultResolution.height")
	
	current_selection = pm.selected()
	currentState = toggleSpeakers(1)
	
	
	#toggle display color
	pm.displayRGBColor("background", 0.0, 0.0, 0.0)
	
	#get current camera
	activeView = pm.playblast(activeEditor=1)
	activeCamera = pm.modelEditor(activeView, q=1, camera=1).name()
	
	camNameParts = activeCamera.split("_") 
	
	pbVersion =""
	for camNamePart in camNameParts:
		if camNamePart[0] == "v":
			pbVersion = camNamePart
			
			
	startTime = int(camNameParts[-2])
	endTime = int(camNameParts[-1])
	
	setTimeline()
	
	pm.select(cl=1)
	
	pathWithVersion = "X:/Projects/GREY11_ANM71_Rewe_Starzone/GR11A71_Shots/GR11A71_Animatic/Animatic_Maya/data/%s/" % pbVersion
	playblastPath = pathWithVersion+activeCamera
	
	
	#make playblast
	pm.playblast(
		filename = playblastPath,
		format = "movie",
		width = renderWidth,
		height = renderHeight,
		percent = 100,
		compression = "none",
		quality = 100,
		forceOverwrite = 1,
		offScreen = 1,
		framePadding = 4,
		startTime = startTime,
		endTime = endTime,
		showOrnaments=0
	)
	
	
	
	pm.displayRGBColor("background", 0.632, 0.632, 0.632)
	
	
	pm.select(current_selection, r=1)
	
	toggleSpeakers(currentState)
	

def prefRun():
	'''prefix script run with script name und datetime
	'''
	print '\n\n\n',proc_name,
	print datetime.now(),'##'


def setTimeline():
	#get current camera
	activeView = pm.playblast(activeEditor=1)
	activeCamera = pm.modelEditor(activeView, q=1, camera=1).name()
	
	camNameParts = activeCamera.split("_") 
	
	startTime = int(camNameParts[-2])
	endTime = int(camNameParts[-1])
	
	pm.playbackOptions(
		animationEndTime=endTime,
		animationStartTime=startTime,
		maxTime=endTime,
		minTime=startTime
		)

def toggleSpeakers(value):
	speakerCtrls = pm.ls("SPEAKERANIMATION")
	currentState = 0

	for speakerCtrl in speakerCtrls:
		currentState = pm.getAttr(speakerCtrl+".geoVisibility") 
		pm.setAttr(speakerCtrl+".geoVisibility", value)
		
	
	return currentState
	


