# write a python program to print the contents of a directory using the os module.
# search online for the function which does that



# we are using chatgpt 

# import os
# #specify the directory you want to list
# path = '/web development'

# #lIST ALL files and directories in the specified path
# contents = os.listdir(path)

# #Print all files and directories in the specified path
# print(contents)

import os
#specify the directory you want to list
directory_path = '/web developmemt'

#lIST ALL files and directories in the specified path
contents = os.listdir(directory_path)

#Print all files and directories in the specified path
for item in contents:
        print(item)


