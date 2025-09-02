# Write a program to find out whether a given post is talking about "Harry" or not


#post =" hey  jerry bhai is good JERRY is very good and Jerry is great "
post =input(" Enter the post ")


if("Jerry".lower() in post.lower() ):  # to make lower case all
    print("This post is talking about Jerry")
    
else:
    print(" This post is not talking about jerry")