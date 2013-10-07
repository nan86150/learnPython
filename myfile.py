# coding utf8

fp = file('test.txt', 'a+')
print fp.encoding
fp.write("\r\n")
fp.write("hello")
print fp.encoding
fp.close