# copy file 

from sys import argv
from os.path import exists


script,file1,file2 = argv

#copy from file1 to file2

# open both the file
#check if (paste) file exists or not
#read 
#close

#If the paste file doent exist it will create it 
# So lets check whether file1 exists or not
print(exists(file1))

print("Hit Enter to continue or Ctrl+C to quit")
input()
copied=open(file1).read()


f2 = open(file2,'w')
paste = f2.write(copied)
print(paste) #it will print number of characters
print(len(copied)) # length in number of bytes SAME

f2.close()


'''
indata = open(from_file).read(), which means you don't need to then do in_file.close() when you reach the end of the script. It should already be closed by Python once that one line runs.
'''

