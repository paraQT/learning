people = 15
cars = 30
trucks = 40

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")   # only if previous check returned False
else:
    print("We can't decide.")               # only if previous checks also returned False
# if muultiple (el)ifs are true then only the 1st works
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
