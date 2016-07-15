# paratmeter unpacking variables

# Example-1  Use of argv i.e. argument variable
from sys import argv 

# assign variables to argv to unpack
a = argv    # incase you want different name
script,var1,var2,var3 = a
print("Script Name:",script)
print("Variable1:",var1)
print("Variable2:",var2)
print("Variable3:",var3)



