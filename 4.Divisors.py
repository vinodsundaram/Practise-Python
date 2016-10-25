# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:17:31 2016

@author: Vinod
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""
num = int(input("Enter a number to list its divisors:"))
x=range(1,num+1)
## range is one less than num

div=list()
for item in x:
    if num%item ==0:
        div.append(item)

print("the divisors of",num,"are:", div)
