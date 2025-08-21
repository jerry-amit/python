# d={} # empty dictionary
marks ={
    "jerry" :100,
    "shivam":38,
    "satyam":80,
    "list":[1,2,3,45]
    }

# print(marks.items())  # We can print items Value also Add add value also
# print(marks.keys())  # We can print keys Value also
# print(marks.values())  # We can print values also

# marks.update({"jerry":99 ,"renuka":98}) # we can update the value by this Add add value also
# print(marks)

# print(marks.get("jerry2")) # Check if data is not present then it will return None either present then the value

#value = marks.pop("jerry","default_value")
item = marks.popitem()   #pop item list
print(item)
print(marks)

#Using pop method()
Value = marks("jerry")
print(Value)
print(marks)

d={0:1,1:"jerry"}
len(d)
print(len)