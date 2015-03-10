__author__ = 'vladymyr'
import unittest
from CompArcLab1 import MyXmlParser
from CompArcLab1 import conf
import xml.etree.ElementTree as ET

test_file_path = "/home/vladymyr/Documents/PythonRssXMLSimpleNewsFeeder--master/UnitTest/FirstTest.py"



class MyTest(unittest.TestCase):
    def test_getUrlPath(self):
        str = conf.getUrlPath()
        self.assertEqual(str, '/home/vladymyr/Documents/CompArcLab1-master/CompArcLab1/source/urls.xml')

    def test_InfoPath(self):
        str = conf.getInfoPath()
        self.assertEqual(str, '/home/vladymyr/Documents/CompArcLab1-master/CompArcLab1/gns/data.txt')


    def test_getDirectChildrenTagText(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/PycharmProjects/CompArcLab1/CompArcLab1/source/urls.xml')
        urlList = xmlParser.getDirectChildrenTagText("url")
        self.assertEqual(len(urlList), 6)
        self.assertEqual(urlList[0], ('http://www.npr.org/rss/rss.php?id=1004', 'npr'))

    def test_searchForInfo(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/PycharmProjects/CompArcLab1/CompArcLab1/source/urls.xml')
        file = open('MyTestRSS.xml', 'r')
        text = file.read()
        rss = ET.fromstring(text)
        for item in rss.iter('item'):
            for child in item:
                content = child.text
                if (child.tag == "title" or child.tag == "description"):
                    self.assertEqual(xmlParser.searchForInfo(content, conf.getInfoList()) , True)

        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/PycharmProjects/CompArcLab1/CompArcLab1/source/urls.xml')
        file = open('MyTestRSS2.xml', 'r')
        text = file.read()
        rss = ET.fromstring(text)
        for item in rss.iter('item'):
            for child in item:
                content = child.text
                if (child.tag == "title" or child.tag == "description"):
                    self.assertEqual(xmlParser.searchForInfo(content, conf.getInfoList()) , False)


    def test_findWholeWord(self):
        xmlParser = MyXmlParser.myXMLParser('/home/vladymyr/PycharmProjects/CompArcLab1/CompArcLab1/source/urls.xml')
        res = xmlParser.findWholeWord('word')('one ttt word')
        self.assertTrue(xmlParser.findWholeWord('word')('one ttt word'))
        self.assertFalse(xmlParser.findWholeWord('word')('one ttt '))

