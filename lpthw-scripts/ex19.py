def cheese_and_crackers(cheese_count, boxes_of_crackers):       # this function when called prints 4 lines
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)                                     # 20 cheese, 30 crackers

print("OR we can use variables from your script:")              # cheese_and_crackers(10, 50)
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do maths inside too:")
cheese_and_crackers(10 + 20, 5 + 6)                             # cheese_and_crackers(30, 11)

print("And we can combine the two, variables and maths:")       # cheese_and_crackers(110, 1050)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
