# Write a Guru Ram to calculate the grade of a student from his marks from the following scheme:
# 90 -100 =>Ex 80-90 =>A 70-80 =>B 60-70=>C 50-60=>D <50  =>F

marks = int(input("Enter your Marks :"))

if(marks<=100  and marks>=90):
    grade = "Ex"
    
if(marks<90  and marks>=80):
    grade = "A"
if(marks<80  and marks>=70):
    grade = "B"
if(marks<70  and marks>=60):
    grade = "C"
if(marks<60  and marks>=50):
    grade = "D"
if(marks<50):
    grade = "F"
    
    
print("Your Grade is :",grade)