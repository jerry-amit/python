#from advance typing

from typing import List, Tuple, Dict, Union
 # List of integers 
number : List[int] = [1,2,3,4,5]

# Tuple of a string ANd a Integer
person: Tuple[str,int] = ("Alice",30)

#Dictionary with string keys and integer values
Scores: Dict(str,int) = {"Alice": 90, "Bob": 85}

#Union type for Variables that can hold multiple types
identifier: Union[int,str] = "10123"
identifier = 12345 # Also Valid

'''
n : int = 5

name : str = "Jerry"

def sum(a: int,b: int) -> int:
    return a+b

sum(3,4)
print(sum)'''
