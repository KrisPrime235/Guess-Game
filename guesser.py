import random
number = random.randint(1,9)
chances = 0
while chances < 5: 
    guess = int(input("Guess the number!(Any number between 1 and 9) : "))
    chances = chances + 1
    if guess == number:
        print("CONGRATULATIONS! You have guessed the right number")
        break
    else :
        print("Try Again!")
if not chances < 5:
    print("You LOSE! The number was",number)    
