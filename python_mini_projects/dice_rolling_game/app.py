import random

while True:
    choice = input("Do you want to roll the dice? (yes/no): ").lower()
    if choice == 'yes':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, Die 2: {die2}")
    elif choice == 'no':
        print("Thank You for playing!")
        break
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")