import random
from turtle import clear

print("🎮 Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Too low! ⬆️")
    elif guess > secret:
        print("Too high! ⬇️")
    else:
        print(f"🎉 Correct! The number was {secret}.")
        print(f"You guessed it in {attempts} attempts.")
        break