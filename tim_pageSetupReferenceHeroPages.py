#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_pageSetupReferenceHeroPages;reload(tim_pageSetupReferenceHeroPages);tim_pageSetupReferenceHeroPages.main()

"""
tim_pageSetupReferenceHeroPages.py

Created by Tim Reischmann on 2011-10-26.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

"""


import pymel.core as pm
import maya.cmds as mc
from datetime import datetime

#Global Var definitions
proc_name = '## tim_pageSetupReferenceHeroPages: '

def main():
	prefRun()
	
	referenceHeroPages()
	
	
	
	
def prefRun():
    '''prefix script run with script name und datetime
    '''
    print '\n\n\n',proc_name,
    print datetime.now(),'##'
    
def referenceHeroPages():
	mc.file(
		"X:/Projects/GREY11_ANM71_Rewe_Starzone/GR11A71_Shots/GR11A71_Animatic/Animatic_Maya/scenes/05_Rigging/GR11A71_heroPages_Rigging_v002_tR.mb",
		reference=1,
		r=True,
		namespace="hp"
		)
