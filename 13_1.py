'''
1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
2.Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
'''

from sys import argv


script,name_of_the_poem,var1,var2=argv

print("Enter the Name of the Poem:",name_of_the_poem)

print("\n",25*'_*_',"\n")

print("""%s \n\t 
A million %s up in the sky
one shines brighter I can't deny
A %s so precious, a %s so true
a %s that comes from me to you...
""" %(name_of_the_poem,var1,var2,var2,var2
     ))


'''
From My heart
A million stars up in the sky
one shines brighter I can't deny
A love so precious a love so true
a love that comes from me to you...

'''