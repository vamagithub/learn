# open file in write mode and add some content


print("Write the name of the file you want to write content on:")
filename = input()

print("\n\t")

content = open(filename,'w')

# automaticaly empties the pre- existing content

content.write(input("Name of the Song"))
content.write(input("\n\tLyrics:\n\t"))
content.close()

content= open(filename)
print(content.read())

print("Now Go To Sleep ! Good Night")



