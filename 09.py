days = 'Mon Tue Wed Thu Fri Sat Sun'
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
m = "%r\n%r\n%r\n"
print(m % ("a","b","c"))
print("Here are the days %r:" % days)
print('Here are the months:',months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

'''
Why do the \n newlines not work when I use %r?
That's how %r formatting works; it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.
'''