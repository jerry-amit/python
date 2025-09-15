''' The game() function in a program lets a user play a game and returns the score as an integer. you need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() functions breaks the high score.'''

import random

def game():
    print("You Are Playing the game:")
    score =random.randint(1,62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
            
        else:
            hiscore = 0
    print(f"your Score:{score}")
    if(score>hiscore ):#or hiscore==""):
        #Write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score
game()
