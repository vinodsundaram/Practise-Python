# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:21:12 2016

@author: Vinod
"""
string = input("Enter a word:")
revstring=string[::-1]
#print(revstring)

if(string == string[::-1]):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
