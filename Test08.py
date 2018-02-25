# Use the file name mbox-short.txt as the file name

fh = open('mbox-short.txt')
count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
        
    count = count + 1
    value = float(line[line.find('0'):])
    total = total + value
    average = total/count

print ('Average spam confidence: %s' % average)


