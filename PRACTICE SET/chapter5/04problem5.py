# What will be the length of the following set s:

s= set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(s)   # because 1 == 1.0 (true)
print(len(s))   # because 1 == 1.0 (true)
