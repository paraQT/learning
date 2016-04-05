from sys import argv        # loads argv vars from sys module
script, filename = argv     #sets the argv vars

print("We're going to erase %r" % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")
input("?")

print("Opening the file...")
target = open(filename, 'w')    #opens filename with the "write" flag

print("Truncating the file. Goodbye!")
target.truncate()       # truncates/deletes the file

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")

target.write(line1)     # we can write to files because of the "w" flag
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()          # this closes the file
