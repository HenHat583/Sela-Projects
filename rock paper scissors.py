import random

action = int(input("WELCOME TO ROCK PAPER SCISSORS\n please insert a number that represent an action:\n 1 for paper\n 2 for rock\n 3 for scissors:\n"))
bot_action = random.choice([1, 2, 3])
yes = True
while yes:
    if action == bot_action:
        print("tie")
    elif action == 1 and bot_action == 2:
        print("loss(bot chose paper)")
    elif action == 1 and bot_action == 3:
        print("WIN(bot chose scissors)")
    elif action == 2 and bot_action == 1:
        print("WIN(bot chose rock)")
    elif action == 2 and bot_action == 3:
        print("loss(bot chose scissors)")
    elif action == 3 and bot_action == 1:
        print("loss(bot chose rock)")
    elif action == 3 and bot_action == 2:
        print("WIN(bot chose paper)")
    choise = input("do you want to start a new game? y/n: ")
    if choise == "n":
        break
    else:
        action = int(input("WELCOME TO ROCK PAPER SCISSORS\n please insert a number that represent an action:\n 1 for paper\n 2 for rock\n 3 for scissors:\n"))
