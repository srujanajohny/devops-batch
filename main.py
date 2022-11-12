# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:17:30 2022

@author: tanay
"""

a = 1 #integer
b = 2.0 #float
c = 'abc' #string
d = "def" #string


# print(a, b, c, d)

# H.W. :: All the data types in python

# ______________________DATA STRUCTURES _____________________________

l = [1,2,3,4, 3, 4,5] #list, mutable
t = (12,3,45,0,23,23,23,2) # tuple, immutable
s = {1,2,3,4,4,5,5} #set
d = {1:1, 2:2, 2:4, 4:1} #dictionary


# print(l)
# print(t)
# print(s)
# print(d)

# H.W. :: All the data structures in python
# ________________________________________________________________

# LIST: Data strucuture in python, to hold the data in continous fashion in the memory
# it can have duplicates
# it can be changes, hence it is mutable
# it has mutliple functions and can be looped



l = [4, 12, 21, 2121,12,12,1,1,5]

print(l)
print(l.index(2121))
print(l[2])
print(len(l))
print(l*2)
l.reverse()
print(l)


l.sort()
print(l)
# H.W.: how to sort a list in descending order?