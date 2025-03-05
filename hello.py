import random
print("Hello")

answer = random.randint(1,5)
guess = int(input("Please enter an integer: "))
while (answer != guess):
    print("You are wrong.")
    guess = int(input("Please enter another integer:"))
print("You are right!")
