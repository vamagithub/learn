# -*- coding: utf-8 -*-
# 15_Reading_Files.py

from sys import argv

script, filename= argv
 
print("File you want to open is %s : " % filename)

# 1. Open File open(filename)
# 2. Read File var.read()
# 3. Close after reading var.close()

text = open(filename)
# text is a file object which will use fucntions like read,close etc..

print(text.read())
text.close()


