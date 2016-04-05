print("You enter a dark room with two doors. Do you go through door #1, #2 or #3?")
door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")

    if insanity == "1":
        print("Your body survives powered by a mind of jelly. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

elif door == "3":
    print("You've entered a tomb with dwarven remains. What do?")
    print("1. Turn back and leave.")
    print("2. Go deeper into the tomb.")
    dead = input("> ")

    if dead == "1":
        print("You are killed by a squid like creature. The end.")
    if dead == "2":
        print("You knock over a metal chain and the noise summons a horde of orcs. The end.")
    else:
        ("You decide to do nothing but wait here. You run out of supplies and die eventually.")
else:
    print("You stumble around and fall on a knife and die. Good job!")
