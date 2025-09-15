#Write a program to read text from given file 'poems.txt' and find out whether it contains yhe word 'twinkle'

f = open("poem.txt")
content = f.read()
if("twinkle " in content):
    print(" the word Twinkle is present in the content :")
    
else:
    print(" the word Twinkle is not present in the content :")
f.close()