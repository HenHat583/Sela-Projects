import random
guess = int(input("please guess a number: "))
number = random.choice(range(9))
yes = True
count = 0

while yes:
    count = count + 1
    if guess < number:
        print("oops! you lost. you guessed a lower number!")
        guess = int(input("please guess a number: "))
    elif guess > number:
        print("oops! you lost. you guessed a higher number!")
        guess = int(input("please guess a number: "))
    elif guess == number:
        print("Congratulations! You won! And it only took you",count, "tries!")
        break