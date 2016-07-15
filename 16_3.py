'''
There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
'''

# if you want to write into file open file using 'w' parameter , bcoz by default it will open with read mode only
filename = input("Enter file name you wnat to open")
filename = open(filename,'a+')
print(filename.read())

poem = input("Poem Name:")
para = input("Poem Lyrics:")

filename.write("%s\n\t%s"%(poem,para))
print(filename.read())
filename.close()


'''
w -write only after erasing everything(truncate)
r- read only (by default)
a/a+ - append write
w+ - erase all and write
r+ - write from start point and substitutes that space with new write content/ appends-
can read and write both
'''