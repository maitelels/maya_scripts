#!/usr/bin/env python
# encoding: utf-8
#LTB:import tim_pageSetup;reload(tim_pageSetup);tim_pageSetup.main()

"""
tim_pageSetup.py

Created by Tim Reischmann on 2011-10-26.
Copyright (c) 2011 Tim Reischmann. All rights reserved.

usage:
import tim_pageSetup;reload(tim_pageSetup);tim_pageSetup.main()

set:
jointLength = 12
jointNumber = 8
pages = 5

in main()

"""


import pymel.core as pm
from datetime import datetime

#Global Var definitions
proc_name = "## pageSetup: "
jointLength = 12.0
jointNumber = 12
paperWidth = 12.0
paperLength = jointLength
pages = 34
#pages = 4
degree = 90
UVnormalized = 1
paperSubdivisionsX = 2 
paperSubdivisionsY = jointNumber
ctrlRadius = 7.0
jacketBack = 2.3
jacketWidth = 12.8
bookmodel = "X:/Projects/GREY11_ANM71_Rewe_Starzone/GR11A71_Shots/GR11A71_Animatic/Animatic_Maya/Scenes/album_v002.ma"
jacketAttr = ['openL', 'openR', 'bendL', 'bendR', 'twistL', 'twistR']

def main():
	prefRun()
	#pm.importFile(bookmodel)
	containers = createContainers("book")
	
	rigBook(containers)
	rigJacket(containers)
	
	
	organizeContainers(containers)
	
	#moveEnds()
	#movePages()
	pm.select('world_ctrl', r=1)

def buildJacket():
	planeBack = pm.polyPlane(
		width=jacketBack,
		height=paperLength,
		subdivisionsX=paperSubdivisionsX,
		subdivisionsY=paperSubdivisionsY,
		axis=(0, 1, 0),
		createUVs=UVnormalized,
		ch=1,
		name="planeBack"
		)
	
	planeLeft = pm.polyPlane(
		width=paperWidth,
		height=paperLength,
		subdivisionsX=jointNumber,
		subdivisionsY=paperSubdivisionsY,
		axis=(1, 0, 0),
		createUVs=UVnormalized,
		ch=1,
		name="planeLeft"
		)
	
	pm.move(planeLeft, (((jacketBack/2)*-1),paperLength/2,0))
	
	planeRight = pm.polyPlane(
		width=paperWidth,
		height=paperLength,
		subdivisionsX=jointNumber,
		subdivisionsY=paperSubdivisionsY,
		axis=(1, 0, 0),
		createUVs=UVnormalized,
		ch=1,
		name="planeRight"
		)
	
	pm.move(planeRight, (((jacketBack/2)),paperLength/2,0))
	
	jacket = pm.polyUnite(planeBack, planeRight, planeLeft,
		ch=0, name="jacket_geo")
	
	pm.select(cl=1)
	
	return jacket

def createContainers(rigName):
	#create containers for the geo and rig
	baseGroup = pm.group(empty=1, name=rigName)
	rig = pm.group(empty=1, name='rig')
	geo = pm.group(empty=1, name='geo')
	paper_grp = pm.group(empty=1, name='paper_grp')
	pages_grp = pm.group(empty=1, name='pages_grp')
	jacket_grp = pm.group(empty=1, name='jacket_grp')
	pageTargets_grp = pm.group(empty=1, name='pageTargets_grp')
	ctrl = createPageCtrl(name='world_ctrl')
	jacket_geo = buildJacket()
	
	geo.inheritsTransform.set(0)
	


	pm.select(cl=1)
	
	return {
		"pageTargets_grp":pageTargets_grp,
		"jacket_geo":jacket_geo,
		'pages_grp':pages_grp,
		'jacket_grp':jacket_grp,
		"ctrl":ctrl,
		"baseGroup":baseGroup,
		"rig":rig,
		"geo":geo,
		"paper_grp":paper_grp,
		}


def rigJacket(containers):
	pm.select(cl=1)
	baseJoint = pm.joint(p=(0,0,0), name="jacketBase")
	
	jacketRight = createJointChain(name='jacketRight')
	pm.select(jacketRight[0], r=1)
	pm.move(0, jacketBack/2, 0)
	pm.select(cl=1)
	
	pm.select(baseJoint, r=1)
	
	jacketLeft = createJointChain(name='jacketLeft')
	pm.select(jacketLeft[0], r=1)
	pm.move(0, ((jacketBack/2)*-1), 0)
	pm.select(cl=1)
	
	#create more attrs
	pm.addAttr(containers["ctrl"],
	ln="__",
	at="enum",
	en="______"
	)
	pm.setAttr(containers["ctrl"]+".__", e=1, keyable=1)
	
	jacketAttrNames = []
	
	#create new attr
	for attr in jacketAttr:
		attrName = containers["ctrl"]+"."+attr
		jacketAttrNames.append(attrName)
		pm.addAttr(containers["ctrl"],
		ln=attr,
		at="double",
		dv=0)
		pm.setAttr(attrName, e=1, keyable=1)
	
	pm.connectAttr( jacketAttrNames[0], jacketLeft[0].rz )
	reverseConnectAttr( jacketAttrNames[1], jacketRight[0].rz )
	
	#connect left jacket bend
	for joint in jacketLeft:
		firstJoint = jacketLeft[0]
		lastJoint = jacketLeft[-1]
		if joint == firstJoint or joint == lastJoint:
			continue
		pm.connectAttr( jacketAttrNames[2], joint.rz )
	
	#connect right jacket bend
	for joint in jacketRight:
		firstJoint = jacketRight[0]
		lastJoint = jacketRight[-1]
		if joint == firstJoint or joint == lastJoint:
			continue
		reverseConnectAttr( jacketAttrNames[3], joint.rz )
	
	#connect left jacket twist
	for joint in jacketLeft:
		firstJoint = jacketLeft[0]
		lastJoint = jacketLeft[-1]
		if joint == lastJoint:
			continue
		pm.connectAttr( jacketAttrNames[4], joint.ry )
	
	#connect right jacket twist
	for joint in jacketRight:
		firstJoint = jacketRight[0]
		lastJoint = jacketRight[-1]
		if joint == lastJoint:
			continue
		reverseConnectAttr( jacketAttrNames[5], joint.ry )
	
	pm.select(baseJoint, r=1, hi=1)
	pm.select(containers["jacket_geo"], add=1, )
	pm.bindSkin(toAll = 1, colorJoints = 1)
	pm.select(cl=1)
	pm.parent(baseJoint, containers["jacket_grp"])
	pm.select(cl=1)
	
def organizeContainers(containers):
	pm.parent(containers["rig"], containers["baseGroup"])
	pm.parent(containers["geo"], containers["baseGroup"])	
	pm.parent(containers["paper_grp"], containers["geo"])
	
	pm.parent(containers["pageTargets_grp"], containers["ctrl"]) 
	pm.parent(containers["pages_grp"], containers["ctrl"]) 
	
	pm.parent(containers["ctrl"], containers["rig"])
	
	pm.parent(containers["jacket_geo"], containers["geo"])
	pm.parent(containers["jacket_grp"], containers["ctrl"])
	
def rigBook(containers):
	center = createJointChain(name='center')
	left = createJointChain(name='left')
	right = createJointChain(name='right')
	ctrl = containers["ctrl"]
	
	pm.addAttr(containers["ctrl"],
	ln="_",
	at="enum",
	en="______"
	)
	pm.setAttr(containers["ctrl"]+"._", e=1, keyable=1)
	
	for page in range(pages):
		pageName = 'page'+str(page)
		skin = createJointChain(pageName+"_")
		rigPage(skin, center, left, right, ctrl, pageName)
		paper = createPaper(pageName)
		pm.select(skin, r=1, hi=1)
		pm.select(paper, add=1, )
		pm.bindSkin(toAll = 1, colorJoints = 1)
		pm.select(cl=1)
		pm.parent(paper, containers["paper_grp"])
		pm.parent(skin[0], containers["pages_grp"])
		pm.select(cl=1)
		print "rigged: %s" % pageName
	
	pm.parent(center[0], containers["pageTargets_grp"])
	pm.parent(left[0], containers["pageTargets_grp"])
	pm.parent(right[0], containers["pageTargets_grp"])


def createPaper(pageName):
    paper = pm.polyPlane(
		width=paperWidth,
		height=paperLength,
		subdivisionsX=paperSubdivisionsX,
		subdivisionsY=paperSubdivisionsY,
		axis=(1, 0, 0),
		createUVs=UVnormalized,
		ch=1,
		name=pageName+"_paper_geo"
		)
    pm.move(paper, 0, paperLength/2, 0)
    
    pm.select(cl=1)
    return paper


def createJointChain(name='joint'):
    number = jointNumber+1
    newChain = []
    for i in range(number):
        jointName = name+str(i+1)
        length = (jointLength/(number-1))*i
        newJoint = pm.joint(p=(0,length,0), name=jointName)
        newChain.append(newJoint)
    pm.select(cl=1)
    return newChain

        
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

def colorCtrl(containers):
	'''colors the control yellow. Ugly! rewrite!
	'''
	pm.select(containers["ctrl"], r=1)
	shape = pm.listRelatives(s)
	pm.setAttr((shape[0]+".overrideEnabled"),1)
	pm.setAttr((shape[0]+".overrideColor"),17)

def prefRun():
    '''prefix script run with script name und datetime
    '''
    print '\n\n\n',proc_name,
    print datetime.now(),'##'

def createPageCtrl(name):
    control = pm.circle(
    	c=(0, 0, 0),
    	nr=(0, 1, 0),
    	sw=360,
    	r=ctrlRadius,
    	d=3, ut=0, tol=0.01, s=8, ch=1,
    	n=name)
    
    pm.move(control, 0, paperLength/2, 0)
    pm.makeIdentity( control, apply=True, translate=True, scale=True, rotate=True)
    
    shape = pm.listRelatives(control)
    shape[0].overrideEnabled.set(1)
    shape[0].overrideColor.set(17)
    
    pm.select(cl=1)
    return name                      

def reverseConnectAttr(leftAttr, rightAttr):
    connector = pm.createNode("multiplyDivide",
    name="connect_"+leftAttr.replace('.','_')+"_"+rightAttr.replace('.','_'))
    
    pm.setAttr(connector.operation, 1)
    pm.connectAttr(leftAttr, connector.input1X)
    pm.setAttr(connector.input2X,-1)
    pm.connectAttr( connector.outputX, rightAttr)

def rigPage(skin, center, left, right, ctrl, pageName):
    '''This will do the actual page setup.
    takes lists of joints: skin, center, left, right
    the name of the ctrl
    and the desired attr name to add to the ctrl
    '''
    
    
    #Variable Definitions
    driveName = ctrl+"."+pageName
    
    #Driven key tangent type
    inTangentType = 'linear'
    outTangentType = 'linear'
    
    #create new attr
    pm.addAttr(ctrl, ln=pageName, at="double", min=-10, max=10, dv=0)
    pm.setAttr(driveName, e=1, keyable=1)
    
    
    for j in range(len(skin)):
        #create a blend weighted node for translate x, y, z and rotate x, y, z
        rx = pm.createNode("blendWeighted", n=(skin[j]+"rx").replace("|", "_"))
        ry = pm.createNode("blendWeighted", n=(skin[j]+"ry").replace("|", "_"))
        rz = pm.createNode("blendWeighted", n=(skin[j]+"rz").replace("|", "_"))
        tx = pm.createNode("blendWeighted", n=(skin[j]+"tx").replace("|", "_"))
        ty = pm.createNode("blendWeighted", n=(skin[j]+"ty").replace("|", "_"))
        tz = pm.createNode("blendWeighted", n=(skin[j]+"tz").replace("|", "_"))

        '''blendWeighted
        is one of those nodes that don't work just yet. You need to assign a value
        to a certain attribute in order for the node to create it. The next section
        will create inputs and weights for translate x, y, z and rotate x, y, z
        '''
        
        #create w[0] weight attributes
        rx.w[0].set(0)
        ry.w[0].set(0)
        rz.w[0].set(0)
        tx.w[0].set(0)
        ty.w[0].set(0)
        tz.w[0].set(0)

        #create w[1] weight attributes
        rx.w[1].set(0)
        ry.w[1].set(0)
        rz.w[1].set(0)
        tx.w[1].set(0)
        ty.w[1].set(0)
        tz.w[1].set(0)

        #create w[2] weight attributes
        rx.w[2].set(0)
        ry.w[2].set(0)
        rz.w[2].set(0)
        tx.w[2].set(0)
        ty.w[2].set(0)
        tz.w[2].set(0)

        #create i[0] input attributes
        rx.i[0].set(0)
        ry.i[0].set(0)
        rz.i[0].set(0)
        tx.i[0].set(0)
        ty.i[0].set(0)
        tz.i[0].set(0)

        #create i[1] input attributes
        rx.i[1].set(0)
        ry.i[1].set(0)
        rz.i[1].set(0)
        tx.i[1].set(0)
        ty.i[1].set(0)
        tz.i[1].set(0)

        #create i[2] input attributes
        rx.i[2].set(0)
        ry.i[2].set(0)
        rz.i[2].set(0)
        tx.i[2].set(0)
        ty.i[2].set(0)
        tz.i[2].set(0)

        #connect target joints to blendweights
        left[j].rx.connect(rx.i[0])
        left[j].ry.connect(ry.i[0])
        left[j].rz.connect(rz.i[0])

        center[j].rx.connect(rx.i[1])
        center[j].ry.connect(ry.i[1])
        center[j].rz.connect(rz.i[1])

        right[j].rx.connect(rx.i[2])
        right[j].ry.connect(ry.i[2])
        right[j].rz.connect(rz.i[2])

        left[j].tx.connect(tx.i[0])
        left[j].ty.connect(ty.i[0])
        left[j].tz.connect(tz.i[0])

        center[j].tx.connect(tx.i[1])
        center[j].ty.connect(ty.i[1])
        center[j].tz.connect(tz.i[1])

        right[j].tx.connect(tx.i[2])
        right[j].ty.connect(ty.i[2])
        right[j].tz.connect(tz.i[2])

        #connect blendweights to their respective connections
        rx.o.connect(skin[j].rx)
        ry.o.connect(skin[j].ry)
        rz.o.connect(skin[j].rz)

        tx.o.connect(skin[j].tx)
        ty.o.connect(skin[j].ty)
        tz.o.connect(skin[j].tz)

        #set driven keys on blendweights
        
        pm.setDrivenKeyframe(rx.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=1)
        pm.setDrivenKeyframe(ry.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=1)
        pm.setDrivenKeyframe(rz.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=1)
        pm.setDrivenKeyframe(rx.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(ry.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(rz.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(rx.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(ry.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(rz.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)

        pm.setDrivenKeyframe(rx.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(ry.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(rz.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(rx.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=1)
        pm.setDrivenKeyframe(ry.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=1)
        pm.setDrivenKeyframe(rz.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=1)
        pm.setDrivenKeyframe(rx.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(ry.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(rz.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)

        pm.setDrivenKeyframe(rx.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(ry.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(rz.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(rx.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(ry.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(rz.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(rx.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=1)
        pm.setDrivenKeyframe(ry.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=1)
        pm.setDrivenKeyframe(rz.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=1)

        pm.setDrivenKeyframe(tx.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=1)
        pm.setDrivenKeyframe(ty.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=1)
        pm.setDrivenKeyframe(tz.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=1)
        pm.setDrivenKeyframe(tx.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(ty.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(tz.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(tx.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(ty.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)
        pm.setDrivenKeyframe(tz.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=-10, v=0)

        pm.setDrivenKeyframe(tx.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(ty.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(tz.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(tx.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=1)
        pm.setDrivenKeyframe(ty.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=1)
        pm.setDrivenKeyframe(tz.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=1)
        pm.setDrivenKeyframe(tx.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(ty.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)
        pm.setDrivenKeyframe(tz.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=0, v=0)

        pm.setDrivenKeyframe(tx.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(ty.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(tz.w[0], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(tx.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(ty.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(tz.w[1], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=0)
        pm.setDrivenKeyframe(tx.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=1)
        pm.setDrivenKeyframe(ty.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=1)
        pm.setDrivenKeyframe(tz.w[2], itt=inTangentType, ott=outTangentType, cd=driveName, dv=10, v=1)

def moveEnds():
    pm.select('left2', r=1, hi=1)
    joints = pm.ls(sl=1)
    for joint in joints:
        joint.rz.set(degree)

    pm.select('right2', r=1, hi=1)
    joints = pm.ls(sl=1)
    for joint in joints:
        joint.rz.set(degree*-1)

def moveEnds2():
	try:
		pm.select('left1', r=1)
		joints = pm.ls(sl=1)
		for joint in joints:
			joint.rz.set(degree-10)
	except:
		pass

	try:
		pm.select('right1', r=1)
		joints = pm.ls(sl=1)
		for joint in joints:
			joint.rz.set((degree-10)*-1)
	except:
		pass
	
	try:
		pm.select('left2', r=1)
		joints = pm.ls(sl=1)
		for joint in joints:
			joint.rz.set(degree-70)
	except:
		pass

	try:
		pm.select('right2', r=1)
		joints = pm.ls(sl=1)
		for joint in joints:
			joint.rz.set((degree-70)*-1)
	except:
		pass
	
	try:
		pm.select('left3', r=1)
		joints = pm.ls(sl=1)
		for joint in joints:
			joint.rz.set(degree-100)
	except:
		pass

	try:
		pm.select('right3', r=1)
		joints = pm.ls(sl=1)
		for joint in joints:
			joint.rz.set((degree-100)*-1)
	except:
		pass
    
def movePages():
    book = pm.ls('world_ctrl')[0]
    for page in range(pages):
    	print page, "|", (book+"."+('page'+str(page)))
        #pm.setAttr(book+"."+('page'+str(page)),-10)
        pm.setAttr(book+"."+('page'+str(page)), pm.getAttr(book+"."+('page'+str(page)))+((20/pages)*page) )


