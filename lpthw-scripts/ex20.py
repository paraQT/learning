from sys import argv

script, input_file = argv

def print_all(f):       # f var is a file
    print(f.read())     # reads the file

def rewind(f):
    f.seek(0)           # looks for the beginning of the file

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")     # prints whatever n line of the file

current_file = open(input_file)

print("First let's print the while file:\n")
print_all(current_file)     # prints the open input file

print("Now let's rewind, kind of like a tape.")
rewind(current_file)        # goes back to the beginning of the file

print("Let's print three lines")
current_line = 1                            # start at line 1
print_a_line(current_line, current_file)    # print_a_line(1, test.txt)
current_line += 1                           # add 1, now at line 2
print_a_line(current_line, current_file)    # print_a_line(2, test.txt)
current_line += 1                           # add 1, now at line 3
print_a_line(current_line, current_file)    # print_a_line(3, test.txt)
