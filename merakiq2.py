my_files=open("people1.exercise.txt","r")
count=0               # count of number of lines in people.exercise.txt
for name in my_files:
    count=count+1
print(count)
my_files.close()

# print(my_files.read())       #to read a file ...