# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:49:36 2022

@author: chandrakant
"""

import re

print("Magical Calculator")
print("Type 'quit' to exit\n")


previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))
        
        
    if equation == 'quit':
        print("GoodBye, See you Soon...!")
        run = False
        
    else:
        equation = re.sub('[a-zA-Z,:()"{}"]', '', equation)
        
        if previous == 0:
            previous = eval(equation)
            
        else:
            previous = eval(str(equation) + equation)
            
            
while run:
    performMath()
    