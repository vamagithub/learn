"""
Coomon Student Questions:

Are the command line arguments strings?

Ans:  Yes, they come in as strings, even if you typed numbers on the command line. Use int() to convert them just like with int(input()).
"""

# Lets try:

'''
A program which will take number as input, 
and do some stupid calculations.
'''
# For more information :

# python -m pydoc sys

from sys import argv

script , a , b =argv

print("Number A : ",a)
print("Number B : ",b)
print("Lets Check their type:",type(a),type(b))

c =int(a) + int(b)
print("Number C : ",c)
print('Lets check type of C:',type(c))

















