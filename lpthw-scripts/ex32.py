the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# goes through the list and prints each number
for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)

# create empty list
elements = []

for i in range(0,6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print("Element was: %d" % i)
