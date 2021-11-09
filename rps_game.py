import random

# Function that allows users to provide input so they can play. It ask the user to pick then the computer picks
def play():
    user=input("It's time to play a game of rock paper scissors. What's your choice? 'r' for rock,'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','s','p'])

# If the user and computer picks the same option
    if user == computer:
        return'It\'s a tie.'

# If r beats s, if s beats p, if paper beats r
    if is_win(user, computer):
        return 'You win :) !'

    #no if statement because you've already passed 2 cases which ends the function
    return 'Better luck next time loser!'

# helper function to see who wins
def is_win(player, computer):
    if (player== 'r' and computer == 's') or (player== 's' and computer== 'p')\
        or (player == 'p' and computer == 'r'):
        return True

print(play())
