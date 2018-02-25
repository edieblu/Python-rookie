name =('regex_sum_272697 2.txt')
text = open(name)
lines = text.read()

import re
y = re.findall('[0-9]+' ,regex_sum_272697 2.txt.read())
count=0
total=0
for i in y:
    count +=1
    total = total + int(i)

print (count, total)
 
    
    

