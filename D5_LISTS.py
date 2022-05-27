# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:29:41 2022

@author: chandrakant
"""

#Introduction to the list

empty_list = list() #This is an empty list, no item in the list
print(len(empty_list)) #0


fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato','potato','cabbage','onion','carrot']
animal_products = ['milk','meat','butter','yoghurt']
web_techs = ['HTML','CSS','JS','React','Node','MongoDB']
countries = ['Finland','India','Denmark','Sweden','Norway']

#print lists and its length
print('Fruits:', fruits)
print('Number of Fruits:',len(fruits))
print('Vegetables:',vegetables)
print('Number of vegatables:',len(vegetables))
print('Animal Products:', animal_products)
print('Number of Animal Products', len(animal_products))
print('Web Technologies:',web_techs)
print("Number of Web Technologies:",len(web_techs))
print('Number of Countries:',len(countries))


#Modifying Lists

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] #we are accessing the firts item using its index
print(first_fruit) #banana
second_fruit = fruits[1]
print(second_fruit) #orange
last_fruit = fruits[3]
print(last_fruit)  #lemon
#last index
last_index = len(fruits)-1
last_fruit = fruits[last_index]


#Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)
print(second_last)































