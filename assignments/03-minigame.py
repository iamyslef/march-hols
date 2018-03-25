import random, sys
#my code is so bad
#i don't know how to program well
#time to read more
print("Let us play a game. I'm thinking of a number between 1-100. You have 7 guesses.")
number = random.randint(1,100)
def guessy(guesses):
    if guesses < 1 or guesses > 100:
        print("That's not between 1-100!")
    elif guesses > number:
        print("Your guess is too high!")
    elif guesses < number:
        print("Your guess is too low!")
    else:
        print("Your guessed that correctly! You have 200 IQ!")
        sys.exit()
    return
count = 7
guess1 = int(input("Guess #1"))
guessy(guess1)
count = 6
guess2 = int(input("Guess #2"))
guessy(guess2)
count = 5
guess3 = int(input("Guess #3"))
guessy(guess3)
count = 4
guess4 = int(input("Guess #4"))
guessy(guess4)
count = 3
guess5 = int(input("Guess #5"))
guessy(guess5)
count = 2
guess6 = int(input("Guess #6"))
guessy(guess6)
count = 1
guess7 = int(input("Guess #7"))
guessy(guess7)
count = 0
print("Sorry, you didn't guess it in 7 tries. But failure is the mother of success, so never give up!")
