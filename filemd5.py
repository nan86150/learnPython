# coding=utf-8

# 计算指定文件的MD5，SHA1，CRC32

import sys;
import hashlib;
import zlib

def GetFileMd5(strFile):
	file = None;
	bRet = False;
	strMd5 = "";
	crc = 0
	strSha1 = ""
	try:
		file = open(strFile, "rb");
		md5 = hashlib.md5();
		sha1 = hashlib.sha1()
		strRead = ""

		while True:
			strRead = file.read(8096);
			if not strRead:
				break;
			md5.update(strRead);
			sha1.update(strRead)
			crc = zlib.crc32(strRead, crc)
		#read file finish
		bRet = True;
		strMd5 = md5.hexdigest();
		strSha1 = sha1.hexdigest()
	except:
		bRet = False;
	finally:
		if file:
			file.close()
	crcStr = '%08x' %(crc&0xffffffff)
	return [bRet, strMd5, strSha1, crcStr];

if "__main__" == __name__:
    strPath = "D:\sketch.png"
    print(GetFileMd5(strPath));
