import random
from art import logo

chosen_number = random.randint(1, 100)
print(logo)
print("\nWelcome to the number guessing game!")
print("\nI'mm thinking of a number between 1 to 100. Can you guess it?")
difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    no_of_attempts = 10
elif difficulty == "hard":
    no_of_attempts = 5
else:
    print("Enter a valid input")


while no_of_attempts != 0:
    guess = int(input(f"\nYou've got {no_of_attempts} attempts. \nMake a guess: "))

    if guess > chosen_number:
        print(f"Too high.")
        no_of_attempts -= 1
    if guess < chosen_number:
        print(f"Too low.")
        no_of_attempts -= 1

    elif guess == chosen_number:
        print(f"\nYou got it! The answer was {guess}")
        break

    
if no_of_attempts == 0:
    print(f"\nYou've ran out of attempts! You loose (The answer was {chosen_number})")

  


