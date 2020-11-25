import random

# Game start
user = str(input("Enter your name: "))
print(f"Hello, {user}")

ratingsf = open('rating.txt', 'r+')
content_list = ratingsf.readlines()

ratingsf.close()

scores = {}
for i in content_list:
    temp = i.split()
    scores[temp[0]] = int(temp[1])

if user in scores:
    pass
else:
    scores[user] = 0

def playJanken4(valid_play_move):
    player_loses = {"rock": "paper",
                    "paper": "scissors",
                    "scissors": "rock"}

    play_move = valid_play_move
    cpu_move = random.choice(list(player_loses.keys()))

    if play_move == cpu_move:
        print(f"There is a draw ({cpu_move})") # +50
        scores[user] += 50
    elif player_loses[play_move] == cpu_move:
        print(f"Sorry, but the computer chose {cpu_move}") # +0
    elif player_loses[play_move] != cpu_move:
        print(f"Well done. The computer chose {cpu_move} and failed") # +100
        scores[user] +=100

def pon():
    valid_moves = ["rock", "paper", "scissors"]
    play_move = str(input())
    if play_move == "!exit":
        print("Bye")
    elif play_move == "!rating":
        print(f"Your rating: {scores[user]}")
        pon()
    elif play_move in valid_moves:
        playJanken4(play_move)
        pon()
    else:
        print("Invalid input")
        pon()

pon()