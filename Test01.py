name = ('mbox-short.txt')
text = open(name)
counts={}
for line in text:
    if not line.startswith('From '): continue
    words = line.split()
    name=(words[1])
    
    counts[name] = counts.get(name,0) + 1

bigcount = None
bigname = None
for name,count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count
print (bigname, bigcount)
    


