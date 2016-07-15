# 16_Reading_Writing_Files.py

from sys import argv
script, filename = argv

print("Erase %s file using command truncate" % filename)
# when you will open a file in 'w' mode it will first erase all the content of the file. no need to use truncate explicitly

# if the file doen't exist it will create it 

target = open(filename,'w')

target.close()
print(25*'---END---')