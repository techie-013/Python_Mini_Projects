import random

range = input("Give Range : ")

if range.isdigit():
    range=int(range)

    if range <= 0 :
        print('Please type a number larger than 0 next time .')
        quit()

else:
    print('Please type a Number next time.')
    quit()

Random_number = random.randrange(0,range )
guesses=0

while True:
    guesses +=1
    user_guess=input("Make a guess : ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please Type a number')
        continue
    if user_guess==Random_number:
        print("Bravo !! You guessed Correct")
        break
    else:
        print('Oops!! Your guess is wrong')
        if user_guess>Random_number:
            print("You wer above the Number")
        else:
            print('You were below the Number')
        continue
print("You got it in ", guesses ,"guesses")