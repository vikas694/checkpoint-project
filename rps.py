import random

choices = {1:"Rock", 2: "Paper",3: "Scissors"}
computer = random.randint(1,3)

print("======================")
print("Rock Paper Scissors")
print("======================")
print("1) Rock")
print("2) Paper")
print("3) Scissors")

player = int(input("Pick a number: "))

if player == computer:
    print("It's a tie.")
    player = int(input("Pick a number: "))

if player == 1 and computer == 2:
    print("You chose: ",1,"\nCPU chose: ",2)
    print("The player lost.")
if player == 1 and computer == 3:
    print("You chose: ",1,"\nCPU chose: ",3)
    print("The player won!")
if player == 2 and computer == 1:
    print("You chose: ",2,"\nCPU chose: ",1)
    print("The player won!")
if player == 2 and computer == 3:
    print("You chose: ",2,"\nCPU chose: ",3)
    print("The player lost.")
if player == 3 and computer == 1:
    print("You chose: ",3,"\nCPU chose: ",1)
    print("The player lost.")
if player == 3 and computer == 2:
    print("You chose: ",3,"\nCPU chose: ",2)
    print("The player won!")


