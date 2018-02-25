name = ('mbox-short.txt')
text = open(name)
counts = {}
for line in text:
    if not line.startswith('From '):continue
    wds = line.split()
    time = wds[5]
    clock = time.split(':')
    hour = clock[0]

    counts[hour]=counts.get(hour,0) + 1

    lst = counts.items()
lst.sort()
for key, val in lst:
    print (key, val)

