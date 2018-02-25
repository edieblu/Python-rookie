from bs4 import BeautifulSoup
import urllib.request
import re

req = urllib.request.Request('http://www.amazon.co.uk/review/top-reviewers/ref=cm_cr_tr_link_next_693?ie=UTF8&page=693', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, "html.parser")

for a in soup.findAll('a'):
    if 'gp/pdp/profile' in a['href']:
        print (a)
 
