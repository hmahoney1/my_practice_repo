# exercise 1
for i in range(1,21):
    if i%3 == 0:
        print(i)

# exercise 2
sum = 0
for i in range(1,51):
    if i%2 == 0:
        sum+=i
print(sum)

# exercise 3
numbers = [5,8,2,15,10,3,7]
for i in range(len(numbers)):
    if numbers[i] > 5:
        print(numbers[i])

# exercise 4

lst1 = [1,2,3,4,5]
lst2 = []
lst2.append(lst1[0])
for i in range(1, len(lst1)):
    lst2.append(lst2[i-1]+lst1[i])
print(lst2)

# exercise 5
newlist = [0,3,8,4,5]
def swap(anylist = []):
    tmp = anylist[0]
    anylist[0] = anylist[len(anylist)-1]
    anylist[len(anylist)-1] = tmp
swap(newlist)
print(newlist)
