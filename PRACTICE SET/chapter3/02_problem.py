#Write a program to fill  in a letter template given below with name and date.
letter = '''
            Dear <|Name|>,
            You are selected!
            <|Date|>
'''

print(letter.replace("<|Name|>","Jerry").replace("<|Date|>","14 sep 2050"))

letter1 = '''
            Dear Name,
            You are selected!
           date
'''
print(letter1.replace("Name","Jerry1").replace("date","01 jan 2026"))