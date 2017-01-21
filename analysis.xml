# -*- coding: utf-8 -*-

import xml.dom.minidom
dom1=xml.dom.minidom.parse('test.xml')
root=dom1.documentElement
book={}

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


#node type
#1	ELEMENT_NODE
#2	ATTRIBUTE_NODE
#3	TEXT_NODE
#4	CDATA_SECTION_NODE
#5	ENTITY_REFERENCE_NODE
#6	ENTITY_NODE
#7	PROCESSING_INSTRUCTION_NODE
#8	COMMENT_NODE
#9	DOCUMENT_NODE
#10	DOCUMENT_TYPE_NODE
#11	DOCUMENT_FRAGMENT_NODE
#12	NOTATION_NODE

#sample xml
#<root version="1.0.1" encoding="UTF-8">
#<!---->
#    <one id="1">
#        <two>HELLO</two>
#	<two>HELLO2</two>
#        <two-2>Well, hello!</two-2>
#	<two-2>Well, hello!</two-2>
#   </one>
#    
#    <one id="2">
#        <two>WHAT ARE YOU</two>
#        <two-2>I'm a bot, silly!</two-2>
#    </one>
#    <one id="3">
#        <two>HI</two>
#        <two-2>HIHI</two-2>
#    </one>
#    <one id="4">
#        <two>HI*</two>
#        <two-2>HIHI</two-2>
#    </one>
#    <one id="5">
#        <two>安安 *</two>
#        <two-2>閉嘴</two-2>
#    </one>
#    
#</root>
