import urllib2

class WebPage:
	def getHtml(self):
		page = urllib2.urlopen("http://www.baidu.com")
		data = page.read().decode('utf-8')
		print data
		print len(data)

if __name__ == "__main__":
	webpage = WebPage()
	webpage.getHtml()