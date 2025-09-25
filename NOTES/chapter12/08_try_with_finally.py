def main():

    try:
        a = int(input("Hey, ENter a Number :"))


    except ValueError as v:
        print("Heyyy")
        print(v)
        
    except Exception as e: 
        print(e)

    finally:
        print("hey i am inside of finally :")
    
main()