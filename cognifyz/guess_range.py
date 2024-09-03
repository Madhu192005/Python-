import random
def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("The lower bound must be less than the upper bound. Please enter again.")
            else:
                break
        except ValueError:
            print("Please enter valid integer numbers.")
            
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
    while True:
        
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        
        if user_guess < lower_bound or user_guess > upper_bound:
            print(f"Your guess is out of bounds. Please guess a number between {lower_bound} and {upper_bound}.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess}.")
            break

guess_the_number()
