import random 
randNumber=random.randint(1,100)
userGuess=None
guesses=0

while(userGuess!=randNumber):
    userGuess=int(input("Enter your Guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it Right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong!.Enter a smaller Number")
    
        else:
            print("You guessed it wrong!.Enter a larger Number")

print(f"You guessed the number in {guesses} gusses")