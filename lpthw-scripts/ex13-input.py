from sys import argv

script, arg1, arg2 = argv

print("What is your name?", end = " ")
firstname = input()
print("Hello %r. These are your arguments: %r %r" % (firstname, arg1, arg2))
