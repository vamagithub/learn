my_name = 'Vama Mehta'
my_age = 22
my_height = 65
my_weight = 130
my_eyes = 'Black'
my_teeth ='White'
my_hair ='Brown'

# %s format string 
print("Let's talk about %s" % my_name)

# %d format interger
print("She's %d inches tall." % my_height)
print("She's %d punds heavy." % my_weight)

print ("Actually that's not too heavy")

print("She's got %s eyes and %s hair." % (my_eyes,my_hair))
print("Her teeth are usually %s depending on the tea." % my_teeth)

print("If i add %d,%d, and %d "
      "I get %d." 
      %(my_age,my_height,my_weight,my_age+my_height+my_weight))

# Study Drills 
'''
Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
'''


# 1 inch = 2.54 centimeters
# 1 pound = 0.453

# converting height in to inches
# weight to Kilograms

print("Weight in Kilograms is: %f "% (my_weight*0.453))
print("Height in Centimeters is: %F "% (my_height*2.54))


'''
'd'	Signed integer decimal.	 
'i'	Signed integer decimal.	 
'o'	Signed octal value.	(1)
'u'	Obsolete type – it is identical to 'd'.	(7)
'x'	Signed hexadecimal (lowercase).	(2)
'X'	Signed hexadecimal (uppercase).	(2)
'e'	Floating point exponential format (lowercase).	(3)
'E'	Floating point exponential format (uppercase).	(3)
'f'	Floating point decimal format.	(3)
'F'	Floating point decimal format.	(3)
'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
'c'	Single character (accepts integer or single character string).	 
'r'	String (converts any Python object using repr()).	(5)
's'	String (converts any Python object using str()).	(6)
'%'	No argument is converted, results in a '%' character in the result.

For more reading - https://docs.python.org/2/library/stdtypes.html#string-formatting

'''

# using round() function 

a = 5.97665
print ("Round of a: %d" % round(a)) 

b = 5.49999
print ("Round of b:",round(b)) 
