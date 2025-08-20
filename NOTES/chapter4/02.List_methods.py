friends = ["Apple", "Orange", 5, 345.06,False, "Akash", "Rohan","False" ]

print(friends)

friends.append("Jerry")

print(friends)


l1 = [1,34,62,2,6,11]
l2 = [1,34,62,2,6,11]
l3 = [1,34,62,2,6,11]
l4 = [1,34,62,2,6,11]
l1.sort()  # short in ascending order
l2.reverse()#short in reverse order
print(l1)
print(l2)
l3.insert (3, 33333)  # TO insert b/w lists such that its index in the list is 3
print(l3) 
print(l4.pop(3))# to delete the element from index eg3 index 3value will deleted & poped value will print
                # a another way
value = l4.pop(3)        
print(value)

print(l4)