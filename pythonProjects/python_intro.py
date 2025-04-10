
# comments + print statement:

print("Hello World!") # can use quotes or apostrophes to print statements
print('Hello World!')
'''
    this also a comment--> three apostrophes for multiple line comment

'''
' is this a comment --> single and double quotes for single line comments (as well as #)'

# variables and assignment
x = 100 # dont need datatype, no semicolon, use underscores for multiple word names, can't start with a number
x = [1,2,3]
x = "string" # assign variable to string via single or double quotes
print(x) # x can be any of these, itll print based on its last assigned value

# constants 
# usually defined with all upercase letters 
# can technically change the value, using all upper case is just a naming technique

# numeric expressions and math module
x = 100 # same + - * /
y = 10
result = x//y # can use // to prevent floating point decimals from being generated--this would result in 10 (integer) instead of 10.0 (fp)
print(result)

print (int(x/y)) # can also use this to convert result to an integer

# modulus (% gives remainder)
# use "variable % 2 == 1 or 2" to check if number is odd or even

min_value = min(1,2,3) # min is a built in function to find minimum of a set
print(min_value) # use underscores for naming instead of the lower-upper case format 

raised = pow(2,3) # raises to to the power of 3 "pow(number, exponent)"
print(raised)
raised = 2**3 # can also use this-- ** means "to the power of..."
print(raised) 

# can import a math library to do other functions like abs, sqrt, min, max, pow, etc.
# use via math.fn_name (ex math.sqrt(4))

# no increment/decrement operators (++ and --) -- instead use +=
# can use for combining variables and even strings
# *=, -=, /=, etc. also work

# if statements
# if statements dont use brackets, need to indent
# colon at the end of the if condition

x = -1 
y = 0

if x < 0:
    print("x is negative")
    y+=1 #equivalent of y++, ++y
elif x > 0:                         # use elif instead of elseif
    print("x is positive")
else:
    print ("x is zero")

start = 10 
end = 100

# use or/and instead of // and && for condition
if x>start and x <end:
    print ("x is within range")
if x<start or x<end:
    print("x is not in range")


# strings 
# can use the + operator to concantenate two or more strings 
my_name = "Harry"
sentence = "Without " + my_name + " there would be no..."
print(sentence)
# can use str(variable) to convert old variable to string
# can access elements of the string by variablename[i]
# can use - numbers referring to the end of the string
# len(string) determines length of the string (number of characters) max index is len(string) - 1 because 0 is included in index
# can use * to produce multiple copies of string
# can compare strings using == 

# 1/16 

# loops
count = 0
while count < 5:
    print(count)
    count += 1

for i in range(1,15,2): # first two numbers determine what i is initialy assigned to, and the last number determines how the number is incremeneted
    print(i, end=" ") # this end = " " is a way to do a space and keep the print in the same row 
print()

lst=[2,4,6,8]

for i in range(len(lst)):
    print(i, lst[i])
print("Number is", i)

for val in lst: # assigns value of the lst index to the variable(val)
    print(val, end=" ")  #does the same as loop above
print()

for i,val in enumerate(lst): #i,val can have any name, variable created dynamically
    print(i,val)

# functions 
def hello_world():
    print("Hello World")
hello_world()

def hello(name):
    print("Hello", name)
hello("Bob")

def hello2(name = "Bob"):
    print("Hello "+name)
hello2()
hello2("Jane")

course = "Platform Computing"
plat = course[0:8] # can slice off the end, or beginning of a string using the brackets
comp = course[9:18] # only includes first 9 components of original string (platform) and last 9 components (computing)
print(plat)
print (comp)


