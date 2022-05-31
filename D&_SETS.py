# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:55:37 2022

@author: chandrakant
"""

"""
Sets
Set is a collection of items. Let me take you back to your 
elementary or high school mathematics lesson. The mathematics 
definition of a set can ne applied also in python. Set is a 
collection of unordered and in-indexed distinct elements.In \
python set is used to store unique items, and it is possible ot find 
the union, inteesection, difference, subset, superset and 
disjoint set among sets.
"""
#Creating a set
#we use curly brackets, {} to create a set or the set() built in function.

#Creating an empty set

st = {}
st = set()

#creating a set with initial items
st = {'item1','item2','item3','item4'}

fruits = {'banana','orange','mango','lemon'}
print(len(fruits))

#Checking an item
#To check if an item exist in a list we use in membership operator
st = {'item1','item2','item3','item4'}
print("Does set st contain item3?", 'item3' in st)


#Adding items to a set
#Once a set is created we cannot change any items and we can also add 
#Additional items

#Add one item using add()

fruits = {'banana','orange','mango','lemon'}
fruits.add('lime')
print(fruits)

#Add multiple items using update().
#The update() allows to add multiple items to a set.

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

"""
Removing items from a Set
We can remove an item from a set using remove() method. if
the item is not found remove() method will raise errors. so it 
is good to cheeck if the item exist in the given set.
However discard() method does't raise any errors.
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('orange')
print(fruits)

#The pop() methods remove a random item from a list and
#it returns the removed item

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop() #removes a random item from the set

 
































































































