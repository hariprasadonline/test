'''
Created on Aug 6, 2015

@author: hmadas
'''
s = "abcdefg"
assert (s[0:4]=="abcd")
assert (s[4:]=="efg")
assert ("abcdefg"[4:0]=="")
assert ("abcdefg"[0:2]=="ab") 



print (s[0:4])
print ("abcdefg"[0:2])
print (s[4:]=="efg")

print ('this is a text plus a number ' + str(10)) 

mylist = ["Linux", "Mac OS" , "Windows"]
# Print the first list element
print(mylist[0])
# Print the last element
# Negativ values starts the list from the end
print(mylist[-1])
# Sublist - first and second element
print(mylist[0:2])
# Add elements to the list
mylist.append("Android")

print ("After add Android") 

# Print the content of the list
for t in mylist:
  print(t) 
  
print ("After removing") 
 
mylist.remove("Android")
# Print the content of the list
for k in mylist:
  print(k) 
  
print ("distinct::") 

mylist1 = ["Linux", "Linux" , "Windows"]
  
# remove duplicates from the list
mylist1 = list(set(mylist1)) 
for l in mylist1:
  print(l) 
