from bs4 import BeautifulSoup
import urllib.request

position = 17
count = 7
url = "http://python-data.dr-chuck.net/known_by_Lauri.html"
taglist = []
urllist = []
urllist.append(url)

 
for i in range(count):
    html = urllib.request.urlopen(urllist[-1])
    soup = BeautifulSoup(html)
    tags = soup('a')
    taglist = list()
    for tag in tags:
        taglist.append(tag)
    url = taglist[position].get('href', None)
    print ('Retrieving: ', url)
    urllist.append(url)
print ('Last Url: ', urllist[-1])


