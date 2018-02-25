from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.Request('http://www.amazon.co.uk/gp/pdp/profile/A35BGQOWVHREX4/ref=cm_cr_tr_tbl_5854_name', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, "html.parser")

a = soup.findAll("a")
for link in a:
    b = "<a href='%s'>%s</a>" %(link.get("href"), link.text)
    print (b.attrs, b.contents)
#    c = b.find_element_by_css_selector(".a-link-normal pr-email")
#    print (c.text)

    
#g_data = soup.findAll("div", {"class": "a-row break-word"})


 
