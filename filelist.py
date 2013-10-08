# coding=utf-8

import os
import os.path

rootdir = "C:\\"

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
	path = path.replace("/","\\")
	if path[-1] != "\\":
		path = path+"\\"
	list = os.listdir( path )
	result = [x for x in list if os.path.isfile( path+x ) ]
	return result

def test(path, xx):
		filelist = getFileList(path)
		dirlist = getDirList(path)
		dir = os.path.abspath(path)
		print "<br>" + xx + dir
		fp.write("<br>" + xx + dir + "\n")
		
		for file in filelist:
			print "<br>" + xx + file + "  " + str(os.path.getsize(dir+"\\"+file))
			fp.write("<br>" + "|--" + xx + file + "\n" + "  " + str(os.path.getsize(dir+"\\"+file)) )
		print ""
		xx = xx + "  "
		for x in dirlist:
			test(dir+"\\"+x, xx) 
	

	

# dir = os.path.abspath("E:\WorkSpace\python")
# print dir
# dir = dir + "\\" + "hh"
# print dir

fp = open("filelist.html","w")
fp.write("<html>" + "\n")
print test("E:\WorkSpace\python", "|--")
fp.close
print os.path.getsize("file.py")
os.system("pause")

# print "Dir"	
# print getDirList(rootdir)
# print "File"	
# print getFileList(rootdir)