import random

def playJanken2():
    player_loses = {"rock": "paper",
                    "paper": "scissors",
                    "scissors": "rock"}

    play_move = str(input())
    cpu_move = random.choice(list(player_loses.keys()))

    if play_move == cpu_move:
        print(f"There is a draw ({cpu_move})")
    elif player_loses[play_move] == cpu_move:
        print(f"Sorry, but the computer chose {cpu_move}")
    elif player_loses[play_move] != cpu_move:
        print(f"Well done. The computer chose {cpu_move} and failed")

playJanken2()