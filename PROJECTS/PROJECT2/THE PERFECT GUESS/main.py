''' We are going to write a program that generates a random number and asks the user to guess it.

If the player's guess is higher than the actual number, The program displays "lower number please". Similarly, if the user's gets too low, the program prints "higher number please" When the user guesses  the correct number, the number program displays the number of guesses the player used to arrive at the number.

HINT : Use the random module.
'''


import random
n = random.randint(1,100)

a=-1
guesses = 1
while(a != n):
    a = int(input("Guess the number:"))
    if(a>n):
        print("Lower NUmber please:")
        guesses +=1     
            
    elif(a<n):
        print("Higher Numbeer please :")
    guesses +=1
        
print(f"You have Guessed the Correct number {n} in {guesses} atempt.")
    