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


#Slicing Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] #it returns all the fruits
#this is also gave the same result as the above
all_fruits = fruits[0:] #if we don't set where to stop it take all the rest
orange_and_mango = fruits[1:3]
orange_mongo_lemon = fruits[1:]


fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] #it returns all the fruits
orange_and_mango = fruits[-3:-1]
orange_mongo_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado'
print(fruits)  #['Avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  #['Avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  #['Avocado', 'apple', 'mango', 'lime']


#Checking items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
does_exist = 'banana' in fruits
print(does_exist)  #True
does_exist = 'lime' in fruits
print(does_exist)   #False


#Append
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits.append('apple')
print(fruits)   #fruits = ['banana', 'orange', 'mango', 'lemon','apple']
fruits.append('lime')
print(fruits)   #['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']  


#Inserting items in list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') #insert apple between orange and mango
print(fruits) #['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')
print(fruits) #['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']


#Removing Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits) #['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits) #['orange', 'mango']


#POP
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()











































































































































































































































































