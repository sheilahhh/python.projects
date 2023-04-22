# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:46:39 2023

@author: User
"""
#for loops are used when you know the number of iterations
#syntax: for i in range(a,b):
        #instruction
# example
#for i in range(1,10):
    #print(i)
    

#fruits=['Melon','Apple' ,'Pineapple','Orange']
#for i in fruits:
    
    #if i == 'Melon':
        #break
    
    #if i == 'Apple':
        #continue
    #print(i)
#nesting


    
for x in range(0,5):
    for y in range(0,x+1):
        print("*", end=" ")
    print()
    
i=0
while i<10:
    print(i, end="")
    i+=3
    
    
