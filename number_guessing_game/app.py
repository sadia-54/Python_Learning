import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")
