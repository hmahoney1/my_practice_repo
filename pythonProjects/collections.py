# lists 
cart=["apples", "bananas", "cherries", "cherries"]
## print(cart)

cart.append("doughnuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
print(cart)
if "pineapple" in cart: # can use if "string" in to check if something in the list
    cart.remove("pineapples")

cart.pop(3) # 3 is the index value, removes 3rd from the top which in this case is doughnuts. # the top is the last element
print(cart)
cart.pop() # will remove the top element when not specified
print(cart)

#list.clear() clears the whole list making it empty 
# list.count() counts the amount of elements containing that string
# list.index() tells where the element is in the list (index number)

cart.reverse() # reverses order of the list
print(cart)
cart.sort() # sorts list by alphabetical order
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")

squares=[]
for i in range(1,10):# for loop iterating through 1-10
    square = i*i
    squares.append(square) # or squares.append(i*i)
print(squares)

squares=[i*i for i in range(1,10)]
print(squares)

b_items=[item for item in cart if item.startswith("b")]
print(b_items)

inventory=[0]*len(cart)
print(inventory)
inventory[0]=100
print(inventory)

# can slice lists just like strings [:3] is up to the third element (not including) and [4:] is the fourth element to the end

# sets --> cant have duplicates. 
number_set=set()
number_set={1,1,2,3,4,0,10,5} # declared with curly brackets
print(number_set)
number_set.add(-10) # stored in order based on magnitude
print(number_set)

num_lst=[1,1,4,5,5,6,6]
no_dups=set(num_lst)
print(no_dups)
no_dups=list(no_dups) # prints the set, as a list, because the list was already changed to a set 
print(no_dups)

ns=sorted(number_set)
print(ns)

# dictionaries
fav_snacks={}
fav_snacks={
    "kathleen":"tortilla chips", 
    "maggie":"pretzels",
    "emily":"buffalo chicken dip",
    "ava":"chocolate"
}
print(fav_snacks)
fav_snacks["wade"]="popcorn"
print(fav_snacks)

print("kathleen's favorite snack is "+fav_snacks["kathleen"])
if "bob" in fav_snacks:
    print("bob's favorite snack is "+fav_snacks["bob"])

for key in fav_snacks:
    print(key+"'s favorite snack is "+fav_snacks[key])
    print(f"{key}'s favorite snack is {fav_snacks[key]}")

# for key, value in fav_snacks.items:
    # print(key,value)

fav_snacks["alice"]=["chips", "nuts"]
print(fav_snacks)
    