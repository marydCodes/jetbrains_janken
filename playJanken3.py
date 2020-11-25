import random

def playJanken3(valid_play_move):
    player_loses = {"rock": "paper",
                    "paper": "scissors",
                    "scissors": "rock"}

    play_move = valid_play_move
    cpu_move = random.choice(list(player_loses.keys()))

    if play_move == cpu_move:
        print(f"There is a draw ({cpu_move})") # +50
    elif player_loses[play_move] == cpu_move:
        print(f"Sorry, but the computer chose {cpu_move}") # +0
    elif player_loses[play_move] != cpu_move:
        print(f"Well done. The computer chose {cpu_move} and failed") # +100

def pon():
    play_move = str(input())
    if play_move == "!exit":
        print("Bye")
    elif play_move == "rock":
        playJanken3(play_move)
        pon() # too much recursive will run out of stack space!
    elif play_move == "paper":
        playJanken3(play_move)
        pon()
    elif play_move == "scissors":
        playJanken3(play_move)
        pon()
    else:
        print("Invalid input")
        pon()

pon()