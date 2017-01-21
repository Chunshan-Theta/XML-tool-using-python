# -*- coding: utf-8 -*-

import xml.dom.minidom


def NodeDecode(RootNode,i=0):
	i=i+1
	for SecondNode in RootNode.childNodes:#one
		if SecondNode.nodeType == 1:
			#print SecondNode.nodeType
			try:
			   for node in SecondNode.childNodes:
			   	print "="*i+SecondNode.nodeName+":"+node.data
				# "=" show the node how many level 
			except:			   
	    		   print ""		
			NodeDecode(SecondNode,i)
		
		
		



dom1=xml.dom.minidom.parse('test.xml')
root=dom1.documentElement

#function 1  auto analysis
NodeDecode(root)

# function 2 human analysis
for nodes in root.childNodes:#one
	#print nodes.nodeName
    	for nodelist in  nodes.childNodes:#two
		if nodelist.nodeType ==1:
		    print nodelist.nodeName+':'+nodelist.childNodes[0].data
print "="*20
for nodes in root.childNodes:#one / root
	#print nodes.nodeName
    	for nodelist in  nodes.childNodes:#two / one
		if nodelist.nodeType ==1 and nodes.getAttribute('id')=="1":
		    	print nodelist.nodeName+':'+nodelist.childNodes[0].data	
