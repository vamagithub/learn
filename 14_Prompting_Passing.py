from sys import argv

script, username = argv
prompt = '$'

print("Hello, %s I am %s scripts."% (username,script))

print("Ans my questions:")
print("Do you like me, %s" % username)
like = input(prompt)

print("Where do you live %s:" % username)
live = input(prompt)

print("What kind of computer do you have %s" % username)
comp = input(prompt)

print("""

Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.

""" % (like,live,comp))