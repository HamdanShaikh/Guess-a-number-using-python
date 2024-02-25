import random  # Import the random module to generate random numbers

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)  # Randomly select an integer between 1 and 100
    attempts = 0  # Initialize the variable to count the number of attempts

    print("Welcome to the Guess the Number game!")
    print("I've picked a number between 1 and 100. Can you guess what it is?")

    while True:  # Loop indefinitely until the correct number is guessed or the program is terminated
        guess = int(input("Enter your guess: "))  # Prompt the user to enter their guess and convert it to an integer
        attempts += 1  # Increment the attempts counter

        if guess < secret_number:
            print("Too low! Try again.")  # Provide feedback if the guess is lower than the secret number
        elif guess > secret_number:
            print("Too high! Try again.")  # Provide feedback if the guess is higher than the secret number
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")  # Congratulate the user if they guess the correct number
            print(f"It took you {attempts} attempts to win the game.")  # Display the number of attempts it took to win
            break  # Exit the loop once the correct number is guessed

if __name__ == "__main__":
    guess_the_number()  # Call the main function to start the game if the script is executed directly
