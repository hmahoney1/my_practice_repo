name = input("Please enter your name") # input function used to take user input, will wait for this input
print("Hello,", name)                  # input function always takes in a string unless converting the input function or converting the variable it is stored to

try:                                   # try catch clause to throw error
    num = int(input("Enter a number")) # use this to cast the input as an integer -- error will be thrown if a string is inputted
    print(num)
    double = num*2
    print(double)
except:
    print("You didn't enter a number ")

# print statements always have a newline at the end, use end='' to disable this (after a comma)
# you can operate on variables within the print statement
# f strings allow you to embed variables within the print string

with open("movies.txt") as file: # opens file with that name, stores contents in the object "file"
    for line in file:
        line = line.strip() 
        print(line)             # can use line.strip() inside of print statement -- both way strip the end of the line from the txt file

with open("heights.txt") as file:
    for line in file:
        info = line.strip().split() # strip removes the newline character of the txt file and split takes each word as an element by splitting at the space characters
        print(info)
        info[2] = int(info[2]) # converting third element of each list (line) to an integer
        print(info)

file_name = input("Enter a file name")
line_count = 1
with open(file_name) as file:
    for line in file: 
        info = line.strip()
        print (f"{line_count}.", info)
        line_count += 1