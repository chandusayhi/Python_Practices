# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:55:26 2022

@author: chandrakant
"""

#TUPLES
#A tuple is a colletion of different data types which is 
#ordered and unchangeable(immutable). Tuples are written with 
#round brackets, (). Once a tuple is created, we cannot change its values.
#We cannot use add, insert, remove methods in a tuple because it is not modifiable(mutable)


# -> tuple(): to create an empty tuple.
# -> count(): to count the number of a specified item in a tuple.
# -> index(): to find the index of a specified item in a tuple.


# Creating a tuple
#Empty tuple: creating an empty tuple.

empty_tuple = ()
empty_tuple = tuple()

#Tuple with initial values
tpl = ('item1','item2','item3')
fruits = ('banana','orange','mango','lemon')

#tuple length
#we use the len() method to get the length of a tuple
tpl = ('item1','item2','item3')
len(tpl)

#Accessing Tuple items
#Positive indexing similar to the list data type we use
#positive or negative indexing to access tuple items

tpl = ('item1','item2','item3')
first_item = tpl[0]
second_item = tpl[1]
print(first_item)

#Negative indexing means beginning from the end, -1 refers
#to the last item, -2 refers to the second last and the 
#negative of the tuple length refers to the first item.

tpl = ('item1','item2','item3')
first_item = tpl[-3]
second_item = tpl[-2]
print(first_item)
print(second_item)


#Slicing Tuples
#We can slice out a ub-tuple by specifying a range of indexes
#where to start and where to end in the tuple, the return value
#will be a new tuple with the specified items.

#Range of positive indexes
tpl = ('item1','item2','item3','item4')
all_items = tpl[0:4]   #all items
all_items = tpl[0:]   #all items
middle_two_items = tpl[1:3]  #does not include item at index 3
print(all_items)
print(middle_two_items)


#Range of negative indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
org_man = fruits[-3:-1]
org_to_the_rest = fruits[-3:]
print(all_fruits)
print(org_man)
print(org_to_the_rest)

#Changing tuple to list
#We can change tuples to list and lists to tuples.
#Tuple is immutable if we want to modify a tuple we should 
#change it to a list

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)  #['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)

#Checking an item in a tuple
#we can check if an item exists or not in a tuple using in,
#it returns a boolean

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits ) #True
print('apple' in fruits)  #False

#Joining Tuples
#we can join two or more tuple using + operator

tpl1 = ('item1','item2','item3')
tpl2 = ('item4','item5','item6')
tpl_final = tpl1 + tpl2
print(tpl_final)

#Deleting tuples
#It is not possible to remove a single item in a tuple 
#but it is possible to delete the tuple itself using del

fruits = ('banana','orange','mango','lemon')
del fruits
print(fruits)




































