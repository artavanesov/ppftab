import random

print("\tWelcome to 'Guess My Number'!")

wins = 0
defeats = 0
play = 1

while play:
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.")

    # set the initial values
    the_number = random.randint(1, 100)
    guess = int(input("\nTake a guess: "))
    tries = 1

    # guessing loop
    while guess != the_number and tries < 3:
        print("It was your try №", tries)
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
        guess = int(input("\nTake a guess: "))
        tries += 1

    if tries == 3:
        print("\nYou Lose! The number was", the_number)
        defeats += 1
    else:
        print("\nYou guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!")
        wins += 1

    print("Your score: wins -", wins, ", defeats -",
          defeats, ", TOTAL Games:", wins+defeats)

    play = int(input("\nPlay again? [0 - no, 1 - yes]"))

input("\n\nPress the enter key to exit.")
