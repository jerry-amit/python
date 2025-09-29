''' 
Write a program to open 3 files 1.Txt,2.Txt,3.Txt. if any of these files are not present, a message without exiting the program must be printed prompting the same.
'''
try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("thank you")