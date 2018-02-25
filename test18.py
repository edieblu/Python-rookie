import bs4, requests

def follow_link(URL):
    res = requests.get(URL)
    soup = bs4.BeautifulSoup (res.text, 'html.parser')
  
    while i < 4:
        elems = soup.findAll("a")
    return elems[2].text.strip()

end = follow_link('http://python-data.dr-chuck.net/known_by_Fikret.html')

print (end)
    
