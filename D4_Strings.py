# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:39:24 2022

@author: chandrakant
"""

#Single line comment

letter = 'p'   # As string be a single character or a bunch of characters
print(letter)   # p
print(len(letter))   #1
greeting = 'Hello World!' #String could be a single quote or duble quote
print(greeting) # Hello World!
print(len(greeting)) #13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)


#Multi String
multi_line = '''I am a teacher and enjoyinh teaching.
I did'nt find anything as rewarding as empowering people,
That is why I created 30 days of python.'''
print(multi_line)


#string Concatenation
first_name = 'Chandrakant'
last_name = 'Hatti'
space = ' '
full_name = first_name + space + last_name
print(full_name)

#checking length of a string using len() builtin functions
print(len(first_name))  #10
print(len(last_name))   #5
print(len(first_name) > len(last_name))  #True
print(len(full_name))


##Unpacking characters
language = 'Python'
a, b, c, d, e, f = language #unpacking sequence characters into variables
print(a) #p
print(b) #y
print(c) #t
print(d) #h
print(e) #o
print(f) #n




 





























