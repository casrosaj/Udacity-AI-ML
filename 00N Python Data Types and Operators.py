# Data Types are Integers, Floats, Booleans, Strings
# Operators are Arithmetic, Assignment, Comparison, Logical
# print() is a built-in function that displays input values as text in the output

# Arithmetic Operators enables math using PEMDAS logic
# PEMDAS: Paranthesis, Exponents, Multiplication/Division, Addition/Subtraction
# "+" Addition
# "-" Subtraction
# "*" Multiplication
# "/" Division
# "%" Modulo (the remainder after dividing)
# "**" Exponent
# "//" Divides and rounds to the nearest integer
# Example: 
# below is calculating the average of 23, 32, and 64
# avg = (23 + 32 + 64)/3
# print(avg)

# Variables enables assignment of values or text
# Examples:
# Example 1
# mv_population = 74728
# print(mv_population)
# Example 2
# x = 3
# y = 4
# z = 5
# or alternatively:
# x, y, z = 3, 4, 5
# print(x, y, z)

# Pythonian Style 
# Pythonian Variable Examples:
# my_height
# my_lat
# my_long

# Assignment Operators: enables variable to assign something to itself
# Examples:
# x = 2
# x += 2 is equivalent to x = x + 2
# x -= 2 is equivalent to x = x - 2
# x *= 2 is equivalent to x = x * 2 ... etc
# print(x)

# Integers and Floats
# int() for integer values
# float() for decimal or floating point values (approximations)
# Examples:
# x = int(4.7) console shows 4
# y = float(4) where y is now a float of 4.0
# type() for finding out a type of data
# print(type(x)) console shows int
# print(type(y)) console shows float

# Booleans
# Bool data type holds one of the values True or False, 1 or 0 respectively

# Comparison Operators make the data type a Bool
# Examples of Bool Comparison Operators:
# 5 < 3 (less than symbol) console shows False
# 5 > 3 (grater than symbol) console shows True
# 3 <= 3 (less then or equal to) console shows True
# 3 >=5 (greater than or equal to) console shows False
# 3 == 5 (equal to) console shows False
# 3 != 5 (not equal to) console shows True

# Logical Operators make the data type a Bool
# Examples of Bool Logical Operators:
# 5 < 3 and 5 == 5 (and) console shows False
# 5 < 3 or 5 == 5 (or) console shows True
# not 5 < 3 (not; flips bool value) console shows True

# Strings are used to enables text and are shows as type str.
# Example 1:
# my_string = 'this is a string!'
# my_string2 = "this is also a string!!!"
# Example 2:
# this_string = 'Simon\'s skateboard is in the garage.'
# print(this_string) console shows...
# Simon's skateboard is in the garage.

# len() Example:
# first_word = 'Hello'
# second_word = 'There'
# print(first_word + " " + second_word) console shows...
# Hello There
# print(len(first_word)) console shows...
# 5

# Index Example:
# first_word[0] console shows H
# first_word(1) console shows e

# len() assigns a integer data type
# len() math example:
# print(len("abba") / len("ab")) console shows...
# 2.5

# String methods are similar to functions like len(), type() and print()
# len(), type() and print() are functions
# .lower(), .islower(), .count(), .find() are methods that are functions called using dot notation
# Examples:
# my_string = 'sebastian thrun'
# my_string.islower() console shows True
# my_string.count('a') console shows 2
# my_string.find('a') console shows 3

# .format() enables putting values into {} embded in strings
# Example 1:
# print('Mohammed has {} balloons'.format(27)) console shows...
# Mohammed has 27 balloons
# Example 2:
# animal = 'dog'
# action = 'bite'
# print('Does your {} {}?'.format(animal, action)) console shows...
# Does your dog bite?
# Example 3:
# maria_string = 'Maria loves {} and {}'
# print(maria_string.format('math', 'statistics')) console shows...
# Maria loves math and statistics

# F-string Formatting simplifies the process of including variables within a string
# Example 1:
# name = 'John'
# print(f'Hello, {name}') console shows...
# Hello, John
# Example 2:
# a = 5
# b = 3
# print(f'The sum of {a} and {b} is {a+b}') console shows...
# The sum of 5 and 3 is 8

# .split() returns a list data container from the input string
# .split() has two arguments (sep, maxsplit)
# sep is seperator which can be whitespace (default) like space, tabl, return, newline
# sep can be a punctuation like comma or dash
# maxsplit is an argument that provides maximum number of splits
# syntax:
# string.split(sep, maxpsplit)
# Example 1:
# new_str = 'The cow jumped over the moon.'
# new_str.split() console shows...
# ['The', 'cow', 'jumped', 'over', 'the', 'moon.']
# Example 2 using '.' as sep:
# new_str.split('.') console shows...
# ['The cow jumped over the moon', '']
# Example 3 using maxsplit of 3
# my_string.split( ,3) console shows ...
# ['The', 'cow', 'jumped', 'over the moon.']