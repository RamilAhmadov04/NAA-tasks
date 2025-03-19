import random
num = random.randint(1, 100)
attempts = 3
for i in range(1, attempts + 1):
    guess = int(input())
    if guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
        print("win")