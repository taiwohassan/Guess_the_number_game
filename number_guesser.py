import random  # Importing the random module to generate a random number.

top_of_range = input("Type a number: ")  # Prompting the user to input the upper limit for the random number range.

if top_of_range.isdigit():  # Checking if the input is a digit (a valid number).
    top_of_range = int(top_of_range)  # Converting the input to an integer if it is valid.

    if top_of_range <= 0:  # Checking if the number is less than or equal to 0.
        print("Please type a number larger than 0 next time.")  # Informing the user that the number must be greater than 0.
        quit()  # Exiting the program if the input is invalid.
else:
    print("Please type a number next time.")  # Informing the user that the input is not a number.
    quit()  # Exiting the program if the input is invalid.

random_number = random.randint(0, top_of_range)  # Generating a random number between 0 and the user-defined upper limit.
guesses = 0  # Initializing the guess counter to 0.

while True:  # Starting an infinite loop for the guessing process.
    guesses += 1  # Incrementing the guess counter on each iteration.
    user_guess = input("Make a guess: ")  # Prompting the user to guess the number.

    if user_guess.isdigit():  # Checking if the input is a valid number.
        user_guess = int(user_guess)  # Converting the input to an integer if it is valid.
    else:
        print("Please type a number next time.")  # Informing the user that the input is invalid.
        continue  # Skipping the rest of the loop and prompting for another guess.

    if user_guess == random_number:  # Checking if the user's guess matches the random number.
        print("You got it!")  # Congratulating the user for guessing correctly.
        break  # Exiting the loop since the correct number was guessed.
    elif user_guess > random_number:  # Checking if the guess is higher than the random number.
        print("You are above the number")  # Informing the user that their guess is too high.
    else:  # If the guess is neither correct nor too high, it must be too low.
        print("You were below the number")  # Informing the user that their guess is too low.

print("You got it in", guesses, "guesses")  # Printing the total number of guesses the user took to get the correct answer.
