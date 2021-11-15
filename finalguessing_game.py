import random

# define a function and x is the parameter that we want to pass inside
# returns random number for us to guess
def guess(x):
    random_number = random.randint(1,x)
# We don't want guess to ever be confused with the number being guessed.
    guess = 0
# A loop till we answer correctly/ when we guess the number.
    while guess != random_number:
# Get the users guess. Fstrings are used to format the string
        guess = int(input(f'Guess a number between 1 and {x}: '))
# If statements gives the users lues on how close they are to the right answer
        if guess < random_number:
            print ('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry guess again. Too high.')
# Breaks out the loop once the user has guessed the number
    print(f'Congrats, The number was {random_number} correctly.Always trust your intuition. ')

guess(20)
