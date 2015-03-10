import MyXmlParser
import conf
import gevent
import urllib
__author__ = 'vladymyr'

def fetch(url):
    xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
    file = urllib.urlopen(url)
    text = file.read()
    print("\n")
    print("read", len(text), "bytes in " + url[1])
    if (text):
        xmlParser.parseRss(text)

class Main:
    def main(self):
        xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
        urlList = xmlParser.getDirectChildrenTagText("url")
        print(urlList)
        for url in urlList:
            file = urllib.urlopen(url[0])
            text = file.read()
            print("\n")
            print("read", len(text), "bytes in " + url[1])
            if (text):
                xmlParser.parseRss(text)



    def multi_thread(self):
        threads = []
        xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
        urlList = xmlParser.getDirectChildrenTagText("url")
        print(urlList)
        for url in urlList:
            threads.append(gevent.spawn (fetch, url[0]))
        gevent.joinall(threads)
m = Main()
# m.main()
m.multi_thread()
