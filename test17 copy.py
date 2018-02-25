
import urllib.request
import xml.etree.ElementTree as ET
total = 0
stuff = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_272699.xml").read()
for i in stuff:
    stuff = ET.fromstring(stuff)
    lst = stuff.findall('comments/comment')
    for item in lst:
        num = (item.find('count').text)
        total = total+int(num)
    print (total)
    
