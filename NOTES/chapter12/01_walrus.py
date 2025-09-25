#Using walrus operator

if(n := len([1,2,3,4,5])) > 3:
    print(f"List is Too long ({n} Elements, expected <= 3)")# Output: List is Too long  (5 Elements , Expected <=3)
    