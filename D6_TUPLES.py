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































