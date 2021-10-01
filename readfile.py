my_files=open("people1.exercise.txt","r")
# name=my_files.read()
# print(name)
# print(my_files.read())      # to fetch all data..
print(my_files.readline(),end="")      # to print on line we use readline .
print(my_files.readline(),end="")     # to fetch second line
print(my_files.readable())