'''
Created on Aug 6, 2015

@author: hmadas
'''
f = open('c:\\temp\\test.csv', 'r')
#print f
for line in f:
    print (line.rstrip())
f.close() 



f1 = open('c:\\temp\\test.csv', 'r')
output = open('c:\\temp\\test1.text', 'w')
for line1 in f1:
    output.write(line1.rstrip() + '\n')
f1.close() 
