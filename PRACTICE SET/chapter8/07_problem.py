# write a Python function to remove a given word from my list and strip at the same time.

# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l
# l=["jerry", " Rohsan ", "Shubham", "an"]

# print(rem(l,"an"))

def rem(l,word):
    n=[]
    for item in l:
       if not(item == word):
           n.append(item.strip(word))
    return n
           
        
l=["jerry", "Rohan", "Shubhan", "an"]

print(rem(l,"an"))