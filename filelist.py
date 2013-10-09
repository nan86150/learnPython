# coding=utf-8

import os
import os.path

rootdir = "E:\WorkSpace\python"
rootdir = "D:"
global filenum
filenum = 0
global dirnum
dirnum = 0

def getDirList( path ):
	path = str( path )
	if path == "":
		return []
	path = path.replace("/","\\")
	if path[-1] != "\\":
		path = path+"\\"
	list = os.listdir( path )
	result = [x for x in list if os.path.isdir( path+x ) ]
	return result

def getFileList( path ):
	path = str( path )
	if path == "":
		return []
	# path = path.replace("/","\\")
	if path[-1] != "\\":
		path = path+"\\"
	print path
	list = os.listdir( path )
	result = [x for x in list if os.path.isfile( path+x ) ]
	return result

def humSize( size ):
	if size/(2**30):
		return "%.2fGB" %(size/float(2**30))
	elif size/(2**20):
		return "%.2fMB" %(size/float(2**20))
	elif size/(2**10):
		return "%.2fKB" %(size/float(2**10))
	else:
		return "%sB" %(size)
		
def test(path, offsets):
		global dirnum, filenum
		dirnum += 1
		filelist = getFileList(path)
		dirlist = getDirList(path)
		dir = os.path.abspath(path)
		fp.write("<br>\t\t\t%s %s\n" %(offsets,os.path.basename(path)) )
		offsets = "│   " + offsets
		
		for file in filelist:
			fp.write("<br>\t\t\t%s %s (%s)\n" %(offsets, file, humSize(os.path.getsize(dir+"\\"+file))))
			filenum += 1

		for xx in dirlist:
			test(dir+"\\"+xx, offsets) 
	

head = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<style type="text/css">
			<!-- 
			BODY { font-family : courier, monospace, sans-serif; }
			P { font-weight: normal; font-family : courier, monospace, sans-serif; color: black; background-color: transparent;}
			B { font-weight: normal; color: black; background-color: transparent;}
			A:visited { font-weight : normal; text-decoration : none; background-color : transparent; margin : 0px 0px 0px 0px; padding : 0px 0px 0px 0px; display: inline; }
			A:link    { font-weight : normal; text-decoration : none; margin : 0px 0px 0px 0px; padding : 0px 0px 0px 0px; display: inline; }
			A:hover   { color : #000000; font-weight : normal; text-decoration : underline; background-color : yellow; margin : 0px 0px 0px 0px; padding : 0px 0px 0px 0px; display: inline; }
			A:active  { color : #000000; font-weight: normal; background-color : transparent; margin : 0px 0px 0px 0px; padding : 0px 0px 0px 0px; display: inline; }
			.VERSION { font-size: small; font-family : arial, sans-serif; }
			.NORM { color: black; background-color: transparent;}
			.FIFO { color: purple; background-color: transparent;}
			.CHAR { color: yellow; background-color: transparent;}
			.DIR  { color: blue; background-color: transparent;}
			.BLOCK { color: yellow; background-color: transparent;}
			.LINK { color: aqua; background-color: transparent;}
			.SOCK { color: fuchsia; background-color: transparent;}
			.EXEC { color: green; background-color: transparent;}
			-->
		</style>
	</head>
	<body>
			<p>文件列表
'''
# tail = '''
		# <br><br>
		# </p>
		# <p>

		# <br><br>
		# </p>
	# </body>
# </html>
# '''
tail = '''
	</body>
</html>
'''


fp = open("filelist.html","w")
fp.write(head)

test(rootdir, "├──")
fp.write("</p><p>%d个文件夹，%d个文件<br><br></p>" %(dirnum, filenum))
fp.write(tail)
fp.close

fp = open("filelist.html","r")
fp.readline()
fp.close

