
import urllib.request
import json
counts = []
stuff = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_272703.json").read()
data = json.loads(stuff.decode('utf-8'))


comments = data["comments"]

for comment in comments:
    counts.append(comment['count'])

print ("Count: {0}".format(len(counts)))
print ("Sum: {0}".format(sum(counts)))
    
