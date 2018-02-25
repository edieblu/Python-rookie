import pyperclip

link = input('link:')
pos = link.find('/dp/')
pos2= link.find('?ie')
cut = (link[pos:pos2])
final = ('https://www.amazon.co.uk'+cut+'/')
pyperclip.copy(final)

    
