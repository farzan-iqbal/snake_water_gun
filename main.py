'''
1 for snake
-1 for water
0 for gun

'''
import random # importing the random module to let the computer choose randomly

computer = random.choice([1 , -1 , 0]) # computer randomly picks: 1 (snake), -1 (water), or 0 (gun)

n = input("enter your choice: ") # taking user's input: 's' (snake), 'w' (water), or 'g' (gun)

youdict = {"s" : 1 , "w" : -1 , "g" : 0} # youdict: converts user’s letter input into a number

reverseddict = {1 : "snake" , -1 : "water" , 0 : "gun"} # reverseddict: converts number back into name (for displaying)

# input check: if the user enters wrong letter
if n not in youdict:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
    exit()

you = youdict[n] # storing the user's choice as a number using the dictionary

print(f"you chose {reverseddict[you]}\n computer chose {reverseddict[computer]}") # printing what the user and the computer chose (in words)

if (computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you ==1):
        print("you win")

    elif(computer == -1 and you==0):
        print("you lose")

    elif(computer == 1 and you == -1):
        print("you lose")

    elif(computer == 1 and you == 0):
        print("you win")

    elif(computer == 0 and you == -1):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you lose")    

    else:
        print("something went wrong")
