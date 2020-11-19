# Stage 1: Unfair computer. Programme should always choose an option that defeats the one picked by the user

def janken1():
    user_input = str(input())
    if user_input == "rock":
        print("Sorry, but the computer chose paper")
    elif user_input == "paper":
        print("Sorry, but the computer chose scissors")
    elif user_input == "scissors":
        print("Sorry, but the computer chose rock")


janken1()