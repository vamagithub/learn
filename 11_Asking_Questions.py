print("What is your name?"),
name = input()
#print("%s" % name)
# Venus
#print("%r" % name)
#'Venus'
#checking the type input provides
surname = input("Enter your surname:")
age = input("Enter your age:")
#so we saw , input() converts every thing in to type string


print("How old are you?")
age = int(input())
print("How tall are you?")
height = int(input())
print ("How much do you weigh?")
weight =int(input())

# using type coercion 
# string to int/float 
print("\n\n")
print("\t %s" % 'Your Deatils:\n')
print("\t\t > \t Full Name:", name,surname)
print("\t\t > \t Age:", int(age))
print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))