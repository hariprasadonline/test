'''
Created on Aug 6, 2015

@author: hmadas
'''
def addMethodTest(a,b):
    return a+b

def addTest(a,b):
    x=5;
    y=10;
    
    return x+y+a+b;

def addFixedValue(a):
  y = 5
  return y +a
  
  

print (addMethodTest(1,2))

print (addFixedValue(1))
print (addTest(1,2))


# This is a text
s= "Lars"
# This is an integer

x=1
y=4

z=x+y 

print (z)
print (s)
print (s.lower())
print (s.upper())
print (s.startswith('L'))
print (s.rstrip())
print (len(s))

import math

print (math.sqrt(2))
