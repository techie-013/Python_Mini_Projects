import random

user_wins = 0
computer_wins = 0
computer_choice="None"

#User Input 
while True:
    user_choice=input("Type Snake/Water/Gun or Q to quit : ")
    user_choice=user_choice.lower()
    if user_choice =="q":
        break

    if user_choice not in["snake","water","gun"]:
        print("Wrong Choice, Enter Again")
        continue

#Computer Choice
    random_number=random.randint(0,2)
    if random_number==0:
        computer_choice="snake"
    elif random_number==1:
        computer_choice="water"
    else:
        computer_choice="gun"      

#Game logic
    #Computer wins
    if user_choice=="snake" and computer_choice=="gun":
        print(computer_choice)
        print("You lost")
        print("Your snake is shot")
        computer_wins=computer_wins+1

    elif user_choice=="gun" and computer_choice=="water":
        print(computer_choice)
        print("You lost")
        print("Your gun is drowned!")
        computer_wins=computer_wins+1

    elif user_choice=="water" and computer_choice=="snake":
        print(computer_choice)
        print("You lost")
        print("Your water is poisoned")
        computer_wins=computer_wins+1

      #User wins  
    elif user_choice=="snake" and computer_choice=="water":
        print(computer_choice)
        print("You won")
        print("You poisoned my water")
        user_wins=user_wins+1

    elif user_choice=="water" and computer_choice=="gun":
        print(computer_choice)
        print("You won")
        print("You drowned my gun")
        user_wins=user_wins+1

    elif user_choice=="gun" and computer_choice=="snake":
        print(computer_choice)
        print("You won")
        print("You shot my snake")
        user_wins=user_wins+1

    #same choice
    else:
        print("Its same")

#score calculation
print("Computer Score is : ", computer_wins)
print("Your Score is : ", user_wins)
if user_wins>computer_wins:
    print("Bravo you won by ",user_wins-computer_wins)
elif computer_wins>user_wins:
    print("Oops! You lost by : ", computer_wins-user_wins)
else:
    print("Its is a tie with both scoring :", user_wins)