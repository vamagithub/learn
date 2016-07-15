filename = input("File You want to read:")
numberline = int(input("Line Number:"))

content = open(filename)

print("Printing %d characters only" % numberline)
print(content.readline(numberline))

print('*****************************')

print("Print all the lines using readlines")
print(content.readlines(numberline))
