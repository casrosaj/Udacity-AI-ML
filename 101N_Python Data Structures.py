# Data Containers- contains data types and other containers
# Lists - data type for mutable ordered sequences of elements
# Lists type are most similar to string type
# Example:
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July", 'August',
# 'September', 'October', 'November', 'December']
# print(months[0])
# print(months[1])
# print(months[7]) console shows...
# January
# February
# August
# Example 2:
# print(months[-1]) console shows...
# December
# Example 3:
# print(month[25]) console shows...
# IndexError: list index out of range

# Slicing Notation- accessing sub sequence of a list
# Slicing means using indices to "slice" off parts of an object like a string or list
# First number is inclusive, second is exclusive
# Example: 
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July", 'August',
# 'September', 'October', 'November', 'December']
# q3 = months[6:9]
# print(q3) console shows...
# ['July', 'August', 'September']
# Example 2:
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July", 'August',
# 'September', 'October', 'November', 'December']
# first_half = months[:6]
# print(first_half)
# ['January', 'February', 'March', 'April', 'May', 'June']
# Example 3:
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July", 'August',
# 'September', 'October', 'November', 'December']
# second_half = month[6:]
# print(second_half) console shows...
# ['July", 'August', 'September', 'October', 'November', 'December']

# Using len() with lists
# Example 1:
# greeting = 'Hello there'
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July", 'August',
# 'September', 'October', 'November', 'December']
# print(len(greeting), len(months)) console shows...
# 11 12
# Example 2:
# greeting = 'Hello there'
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
# 'September', 'October', 'November', 'December']
# print(greeting[6:9], months[6:9])
# 'the' ['July', 'August', 'September']

# Membership Operators- bool that if is "in" or "not in" a variable or container
# Example 1:
# greeting = 'Hello there'
# print('her' in greeting, 'her' not in greeting)
# console shows...
# True False
# Example 2:
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
# 'September', 'October', 'November', 'December']
# print('Sunday' in months, 'Sunday' not in months)
# console shows...
# False, True

# Mutability- refers to whether or not we can change an object once it has been created.
# Mutable - can be changed
# Immutable - cannot be changed
# Lists are mutable
# Example:
# my_lst = [1, 2, 3, 4, 5]
# my_lst[0] = 'one'
# print(my_lst)
# console shows...
# ['one', 2, 3, 4, 5]
# Strings are immutable
# Example:
# greeting = "Hello there"
# greeting[0] = 'M'
# error: "'str' object does not support item assignment."

# Order-  is about whether the position of an element in the object can be used to access the element.
# Both strings and lists are ordered
# Example:
# scores = ["B", "C", "A", "D", "B", "A"]
# grades = scores
# print("scores: " + str(scores))
# print("grades: " + str(grades))
# scores[3] = "B"
# print("scores: " + str(scores))
# print("grades: " + str(grades))
# console shows...
# scores: ["B", "C", "A", "B", "B", "A"]
# grades: ["B", "C", "A", "B", "B", "A"]

# Useful Functions for Lists 1:
# len() returns how many elements are in a list
# max() returns largest number or last alphabetical
# min() retunrs smallest number or first alphabetical
# sorted() returns a copy of list from smallest to largest or alphabetical order

# Join
# join() takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
# Example:
# new_str = "\n".join(["fore", "aft", "starboard", "port"])
# print(new_str)

# .append() adds a string to the end of the list
# Example:
# letters = ['a', 'b', 'c', 'd']
# letters.append('z')
# print(letters)
# console shows...
# ['a', 'b', 'c', 'd', 'z']

# Tuple - data type for immutable ordered elements that can be indexed and sliced
# Example:
# AngkorWat = (13.4125, 103.866667)
# print(type(AngkorWat))
# console shows...
# <class, 'tuple'>
# print("Angkor Wat is at latitute: {}".format(AngkorWat[0]))
# print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

# Sets - data type for mutable unordered *unique* elements that cannot be indexed and sliced
# sets remove duplicates of items in a list
# .add() is used for adding an element to sets
# .pop() removes a random element from a set

# Dictionary - data type for ordered mutable objects that store mappings of unique keys to values that can be indexed using keys
# stores pairs of elements, keys + values
# keys cannot use mutable datatype
# used as dict_name[key] is used for print, displays value
# Example:
# elements = {'hydrogen' : 1, 'helium' : 2, 'carbon' : 6}
# print(elements['carbon'])
# console shows...
# 6
# elements['lithium'] = 3
# print(elements)
# console shows...
# {'hydrogen' : 1, 'helium' : 2, 'carbon' : 6, 'lithium' : 3}
# print('mithril' in elements)
# console shows...
# False
# Example 2:
# animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
# print(animals['dogs'][3])
# console shows...
# 8

#.get looks up values in a dictionary, better than square bracket lookups to avoid errors
# Example:
# elements = {'hydrogen' : 1, 'helium' : 2, 'carbon' : 6}
# print(elements.get('dilithium'))
# console shows...
# None
# print(elements.get('kryptonite', 'There\'s no such element!'))
# console shows...
# "There's no such element!"

# Identity Operators are *is* and *is not*
# is or is not operator returns false or true for a given variable having the same (or not) identity to an element
# Example: 
# elements = {'hydrogen' : 1, 'helium' : 2, 'carbon' : 6}
# x = elements.get('dilithium')
# is_null = x is None
# print(is_null)
# console shows...
# True

# Compound Data Structures - dictionary within a dictionary
# Example 1: 
# elements = {"hydrogen": {"number": 1,
#                         "weight": 1.00794,
#                         "symbol": "H"},
#              "helium": {"number": 2,
#                         "weight": 4.002602,
#                         "symbol": "He"}}
# Access elements as shown: 
# helium = elements["helium"]  # get the helium dictionary
# hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
# You can also add a new key to the element dictionary:
# oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
# elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
# print('elements = ', elements)
# console shows...
# elements =  {"hydrogen": {"number": 1,
#                          "weight": 1.00794,
#                          "symbol": 'H'},
#               "helium": {"number": 2,
#                          "weight": 4.002602,
#                          "symbol": "He"}, 
#               "oxygen": {"number": 8, 
#                          "weight": 15.999, 
#                          "symbol": "O"}}
# Example 2:
# student_records = {
#    'John': {
#        'age': 20,
#        'major': 'Computer Science',
#        'grades': [85, 90, 92]
#    },
#    'Emma': {
#        'age': 19,
#        'major': 'Mathematics',
#        'grades': [95, 88, 91]
#    }
#}
# Adding a new student:
# student_records['Alex'] = {
#    'age': 21,
#    'major': 'Physics',
#    'grades': [80, 85, 88]
#}
# Adding a grade for an existing student:
# student_records['John']['grades'].append(88)
# Printing the updated dictionary:
# print(student_records)