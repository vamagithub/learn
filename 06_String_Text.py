# Excercise 6 String and Text 

x = "There are only %d types of people" % 10
binary = "binary"
do_not = "don't"

y= "i.e. those who know %s and those who %s" % (binary,do_not)

print(x)
print(y)


# %r raw format 
print("I said: %r." % x)
print("I also said %r." % y)


hilarious = False
joke_evaluation = "Isn't that joke funny - %r"


print(joke_evaluation)

print(joke_evaluation % hilarious)

# strint concatenation
x= 'My name is'
y= 'Vama Mehta'

print(x+" "+y)



print("%s"%"hellos")
# hellos 
# string format

x=5
print("%r"%x)

print("%r" % "hellos")
# 'hellos'
# raw format used for debugging

print(type(5))
# type() is used to identify the type of the variable




