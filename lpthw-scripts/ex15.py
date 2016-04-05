from sys import argv        # loads the argv variables from sys module


script, filename = argv     # gets the argument into the variable

txt = open(filename)        # opens the file from argv

print("Here's your file %r:" % filename)    # prints the filename variable
print(txt.read())           # prints the file
txt.close()                 # closes the file

print("Type the filename again:")
file_again = input("> ")    # puts a file name into a variable

txt_again = open(file_again)    # opens the filename from the variable

print(txt_again.read())     # reads and prints the filename
txt_again.close()           # closes the file
