from sys import argv
script, filename = argv

target = open(filename)
content = target.read()
print(content)
target.close()
