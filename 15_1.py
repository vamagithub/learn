# Read file usig keyboard input

prompt = '>>'

print("Enter 'sample1.txt' if you like popoyye.")

print("Enter 'sample.txt' if you like simpsons.")

filename = input(prompt)

filename = open(filename)
read = filename.read()
print(read)
filename.close()

print(10*'-',"THE END",10*'-')

