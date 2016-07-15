'''
3.Combine input with argv to make a script that gets more input from a user. Don't over think it. Just use argv to get something, and input to get something else from the user.
'''

from sys import argv

name_of_the_script,kitane_aadmi_the = argv

print ("Fill in the blanks:")
print("""
If roses were ___ and violets could be ___, 
I'd take us away to a place just for %r.
You'd see my true colors and all that I felt.
I'd see that you could love me and nobody else.
""" % kitane_aadmi_the)

print("Write two of your favourite colors:")
color1 = input("Name Color 1")
color2 = input("Name Color 2")
print("\n",25*'-*-*',"\n")
print("Your Poem Goes like this:\n\t","""
If roses were %r and violets could be %r, 
I'd take us away to a place just for %s.
You'd see my true colors and all that I felt.
I'd see that you could love me and nobody else...

#shitty poem but whatever >_<

""" % (color1,color2,kitane_aadmi_the) )
'''

If roses were red and violets could be blue, 
I'd take us away to a place just for two.
You'd see my true colors and all that I felt.
I'd see that you could love me and nobody else.
'''
