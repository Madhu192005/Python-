import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        elif user_guess == number_to_guess:
            print("Correct!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess}.")
            break

guess_the_number()
