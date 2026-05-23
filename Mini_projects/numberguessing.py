secretnumber= int(input("Enter a number between 1 and 100: "))
attempts=0

print("welcome to the number guessing game")

while True:
    guess= int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < secretnumber:
        print("Too low! Try again.")
    elif guess > secretnumber:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break