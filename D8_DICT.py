# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:50:17 2022

@author: chandrakant
"""
#Dictionaries
"""
A dictionary is a collection of unordered, modifiable(mutable)
paired (key:value) data type

Creating a Dictionary
To create a dictionary we use curly brackets,{} or the dict()
builtin function
"""
#Syntax
emp_dict = {}
#Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


#Example

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

#The dictionary above shows that a value could be any data 
#typestring, boolean, list, tuple, set or a dictionary

#Dictionary Length
#It checks the number of 'Key:value' pairs in the dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person))  #7

#Accessing Dictionary items
#We can access dictionary items by referring to its key name

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
#print(person['city'])

"""
Accessing an item by key name raises an error if the key does not 
exist. to avoid this error first we have to check if a key exist 
or we can use the get method. The get method returns none,
which is a nonetype object data type, if the key does not exist.
"""
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

#Adding items to a dictionary
#We can add new key value pairs to a dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
 

#Modifying items in dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person['first_name'] = 'Eyob'
person['age'] = 252

#Checking keys in a dictionary
#we can use the in operator to check if a key exist in a dictionarey

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print('first_name' in person)
print('city' in person)

#Removing kay and values pairs from a dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person.pop('first_name')
person.popitem()
del person['is_marred']
print(person)
















