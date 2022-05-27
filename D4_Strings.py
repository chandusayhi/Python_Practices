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

#Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) #P
second_letter = language[1]
print(second_letter) #y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) #n

#if we want to start from right end we can use negative indexing,
#-1 is the last item
language = 'Python'
last_letter = language[-1]
print(last_letter) #n
second_last = language[-2]
print(second_last) #o

#Slicing

language = 'Python'
first_three = language[0:3] #starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) #hon

#Another way
last_three = language[-3:]
print(last_three) #hon
last_three = language[3:]
print(last_three)
 

#Skipping character while splitting python strings

language = 'Python'
pto = language[0:6:2]
print(pto) #pto

#Escape Sequence
print('I hope every one enjoying the python challenge. \n Do you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('This is a back slash symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hellow Worls!\"')

##String Methods
#Capitalize(): Converts the first character the string to capital letter

challenge = 'thirty days of python'
print(challenge.count('y')) #3
print(challenge.count('y',7, 14)) #1
print(challenge.count('th'))  #2

#endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))  #True
print(challenge.endswith('tion'))   #False

#expandtabs(): Replaces tab character with spaces, default tab size is 8.

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  #thirty    days   of   python
print(challenge.expandtabs(10))

#find(): returns the index of first occurances of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  #5
print(challenge.find('th'))  #0

#index(): Return the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  #5

#startswith(): checks string starts with the specified string
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  #true

#swapcase(): Converts lower acse letter to upcase letter
challenge = 'thirty days of python'
print(challenge.swapcase())  #THIRTY DAYS OF PYTHON
challenge = 'ThirTy Days OF PythON'
print(challenge.swapcase()) #tHIRtY dAYS of pYTHon



 









































































































































































































