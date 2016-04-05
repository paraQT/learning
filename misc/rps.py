import random
import time

player = input("[R]ock, [P]aper or [S]cissors? ").lower()
computer = random.choice(["Rock", "Paper", "Scissors"])

def game():

    def win():
        print("You win!")

    def tie():
        print("It's a tie. You both lose!")

    def lose():
        print("You lose. Ahahaha!")

    def countdown():
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

    if player[:1] in ("r"):
        countdown()
        print("You picked rock!")
        print("Computer picked %s!" % computer)

        if computer == "Rock":
            tie()
        elif computer == "Paper":
            lose()
        elif computer == "Scissors":
            win()

    elif player[:1] in ("p"):
        countdown()
        print("You picked paper!")
        print("Computer picked %s!" % computer)

        if computer == "Rock":
            win()
        elif computer == "Paper":
            tie()
        elif computer == "Scissors":
            lose()

    elif player[:1] in ("s"):
        countdown()
        print("You picked scissors!")
        print("Computer picked %s!" % computer)

        if computer == "Rock":
            lose()
        elif computer == "Paper":
            win()
        elif computer == "Scissors":
            tie()

    else:
        print("You were supposed to pick Rock, Paper or Scissors. You lose!")

game()
