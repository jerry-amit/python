
'''We all played Snack Quarter Gun game in our childhood if you haven't googled the rules of this game and write a Python program capable of playing this game with the user'''


import random
''' rules
1 for snake
-1 for water
 0 for gun'''

#computer = -1

# for generate random number 
computer = random.choice([-1,0,1])
youstr = input("Enter your choice :") #we will use a string input first

youDict = {"s" :1 , "w": -1 ,"g":0}
reverseDict = {1 :"Snake" , -1: "Water" ,0:"Gun"}


you = youDict[youstr]

print(f"you choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its a draw ")

else:

   ''' if(computer == -1 and you == 1): #(computer - you ) = -2
        print("You win")
    elif(computer == 1 and you == 0):   #(computer - you ) = -1
        print("you Lose !")
        
    elif(computer == 1  and you == 0):  #(computer - you ) = 1
        print("You win")
    elif(computer == 1 and you == -1):  #(computer - you ) = 2
        print("you Lose !")

    elif(computer == 0 and you == -1):  #(computer - you ) = 1
        print("You win")
    elif(computer == 1 and you == 0):   #(computer - you ) = -1
        print("you Lose !")
        
    else:
        print("SOmething went Wrong:")
'''

if((computer - you) == -1 or (computer - you) == 2):
    print("You lose !")
    
else:
    print("You win")