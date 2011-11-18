#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_copyAnimation;reload(tim_copyAnimation);tim_copyAnimation.main()

"""
tim_copyAnimation.py

Created by Tim Reischmann on 2011-11-10.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

usage:
import tim_copyAnimation;reload(tim_copyAnimation);tim_copyAnimation.main()

"""


import pymel.core as pm
from datetime import datetime


def main():
	prefRun()

def isTransform(node):
  if pm.nodeType(node) == "transform":
    return 1
  else:
    return 0

def pl(items):
    '''print a list in a nicer format for debugging
    '''
    for i in items:
        print i
    
def pd(items):
    '''print a dict in a nicer format for debugging
    '''
    for i in items.keys():
	print i,"|", items[i]

def prefRun():
    '''prefix script run with script name und datetime
    '''
    print '\n\n\n',proc_name,
    print datetime.now(),'##'

def reverseConnectAttr(leftAttr, rightAttr):
    connector = pm.createNode("multiplyDivide",
    name="connect_"+leftAttr.replace('.','_')+"_"+rightAttr.replace('.','_'))
    
    pm.setAttr(connector.operation, 1)
    pm.connectAttr(leftAttr, connector.input1X)
    pm.setAttr(connector.input2X,-1)
    pm.connectAttr( connector.outputX, rightAttr)

