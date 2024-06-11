#Guess the number
import random #for generating random number letter alphabet 
target=random.randint(1,100) #generating random number between 1 to 5
while True:
    userChoice= input("Guess the number or Quite=type Q:")
    if(userChoice=="Q"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success : correct guess")
        break
    elif(userChoice<target):
        print("number is too small guess bigger")
    else:
        print("number is too big")
print("Game Over")