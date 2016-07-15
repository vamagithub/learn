#  %r - raw format
a='2' ; b=5 ;c="Hello" ; d=5*6
formatter = "%r %r %r %r"

print(formatter)
print(formatter % (1,2,3,4))
print(formatter % ("One" ,"Two","Three","Four"))
print(formatter % (True,False,"Love Me",'Or Hate Me'))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing",
    "So I said goodnight."    
    ))

print(formatter % (a,b,c,d))
