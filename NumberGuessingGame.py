import random
print("Welcome to the Guessing Game!")


randnum = random.randint(1, 20)

while True:
    for guess in range(6):
        guesses = 5 - guess

        usernum = int(input("Guess an integer between 1 and 20: "))

        if usernum > randnum:
            print("Too high")
        elif usernum < randnum:
            print("Too low")
        else:
            print("You got it! The number was " + str(randnum) + "!")
            break
        print("You have " + str(guesses) + " guesses left.")

        if guesses == 0:
            print("Game Over")