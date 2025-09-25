try:
    a = int(input("Hey, ENter a Number :"))


except ValueError as v:
    print("Heyyy")
    print(v)
    
except Exception as e: 
    print(e)

else:
    print("i am inside else")
    