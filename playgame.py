import random
player_wins = [(1,0), (2,1), (0,2)]
player_loses = [(b,a) for (a,b) in player_wins]

answer_to_values = {"rock" : 0, "paper" : 1, "scissors" : 2}

def play():
    player_choice = input("Rock, paper or scissors? ")
    player_value = answer_to_values[player_choice]

    bot_choice = random.choice(["rock", "paper", "scissors"])
    bot_value = answer_to_values[bot_choice]

    answer_pair = (player_value, bot_value)

    print("You chose", player_choice, "and the computer chose", bot_choice)

    if answer_pair in player_wins:
        print("You win!")
    elif answer_pair in player_loses:
        print("You lose!")
    else:
        print("Its a draw!")

# Activation game
play()
