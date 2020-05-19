####  --- CONTROL FLOW IN PYTHON --- #### 

# control flow syntax makes use of colons and indentation (whitespace) 
# This indentation system is crucial to Python and is what sets it apart from other programming languages 
# if elif else 

## Syntax of an 'if statement'
#if some_condition: 
    #execute some code 
#elif:
    #do something different 
#else:
    #do something else

#if else example 
print("\nIf else example:")
if 200 <= 300:
    print('False')
else:
    print('True')

hungry = False

if hungry:
    print('Feed me!') 
else: 
    print('I am full!')   

#if elif example:
print("\nIf elif else example:")

location = 'work'

if location == 'beach':
    print('Its so nice here!')
elif location == 'work':
    print('It sucks here!')
else:
    print('Home is nice too!')

####  --- LOOPS IN PYTHON --- #### 

### for loop syntax ### 
# my_iterable = [1,2,3]
# for item_name in my_iterable:
    #print(item_name)
print("\nIterating over Lists example:")

mylist = [1,2,3,4,5]

for num in mylist:
    print(1 + num)

mynums = [1,2,3,4,5,6,7,8,9]

for num in mynums:
    if num % 2 == 0:
        print(num)
    else:
        print(f'{num} is an odd number')

print("\nFor loop example:")

my_sum = 0

# print method is outside the for loop; thus result is different from when the print is inside the for loop 
for num in mynums:
    my_sum = my_sum + num
print(my_sum)

# print method is inside the for loop
for num in mynums:
    my_sum = my_sum + num
    print(my_sum)

myname = 'Dorje Damdul'

for letter in myname:
    print(letter)

## Iterating over tuple ##
print("\nIterating over Tuple example:")

mytuple = (1,2,3,4,5)

for tup in mytuple:
    print(tup)

mylist = [(1,2), (3,4), (5,6), (7,8)]

for num in mylist:
    print(num)

# Tuple Unpacking:
print("\nTuple Unpacking example:")

for (a,b) in mylist:
    print(a)
    print(b)

## Iterating over Dictionary ##
print("\nIterating over Dictionary example:")

myinfo = {'name': 'dorje', 'zip': 94804, 'city': 'Richmond'}

for info in myinfo:
    print(info) # this only prints the keys of myinfo 

for value in myinfo.values():
    print(value) # this prints all the values 

for key,value in myinfo.items():
    print(key) # prints out all the keys 

####  --- WHILE LOOPS IN PYTHON --- #### 
# While loops will continue to execute  block of code while some condition remain true 
# syntax
#while ome_boolean_condition:
    #do something 

# combine with else statement
#while ome_boolean_condition:
    #do something 
#else 
    #do something different

print("\nWhile Loop example:")

x = 0

while x < 5:
    print(f'The value of x is {x}')
    x += 1
else: 
    print('X is not less than 5')

###  break, continue and pass  ### 
# we can use break, continue and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:
# break: breaks out of the current closest enclosing loop
# continue: goes to the top of the closest enclosing loop 
# pass: does nothing at all - use it as a place holder 
print("\nContinue in loops example:")

somestring = 'dorje'

for letter in somestring:
    if letter == 'r': # this says if the letter is equal to 'a' then go to top of the closest enclosing and keep printing letters 
        continue
    print(letter)

print("\nBreak in for loops example:")
 
for letter in somestring:
    if letter =='j':
        break
    print(letter)

print("\n'Break' in while loops example:")
x = 1

while x < 5:
    if x == 4:
        break
    print(x)
    x += 1

####  --- USEFUL OPERATORS IN PYTHON --- #### 

print("\nrange function example:")
# range(start, stop[,step]) 
mynum = [1,2,3]

for num in range(10):  # prints up to 10, starting from 0 - 9
    print(num)
print('\n')
for num in range(3,10): # starts at 3 and prints up to 9 
    print(num)

print('\n')
for num in range(0,11,2): # starts at 0, prints up to 10 by step size of 2 
    print(num)

# enumerate() function:
print("\nenumerate function example:")

myname = 'dorje'

for letter in enumerate(myname):
    print(letter)

# or you can use the enumerate function with index  
print('\n')
for index, letter in enumerate(myname):
    print(index, letter)
    
# zip function: zips together 2 or more lists and pairs up the items in those lists 
print("\nZip function example:")

firstlist = [1,2,3]
secondlist = ['a', 'b', 'c']
thirdlist = ['first', 'second', 'third']
for  item in zip(firstlist, secondlist, thirdlist):
    print(item)
# When working with uneven number of items in one list -  zip only goes as far as the lists with the least number of items, and ignores the rest of the extra items in that list 
print("\nSecond zip function example:")

firstlist = [1,2,3,4,5,6,7,8,9]
secondlist = ['a', 'b', 'c']
thirdlist = ['first', 'second', 'third']

for item in zip(firstlist, secondlist, thirdlist):
    print(item)

print("\nThird zip function example:")

print(list(zip(firstlist, secondlist, thirdlist)))

# unpacking lists 
print("\nTuple unpacking example:")

for a, b, c in zip(firstlist, secondlist, thirdlist):
    print(a) # remember 'a' here is the firstlist
    # print(b) # remember 'b' here is the secondlist 
    # print(c) # remember 'c' here is the thirdlist

# 'in' operator
print('x' in [1,2,3])  # returns false 

print('x' in ['x', 'y', 'z'])  # returns true 

# works in a string also 
print('d' in 'dorje')

# also works in dictionaries 
mydictionary = {'name': 'dorje', 'age': 28}
print('age' in mydictionary)
print(28 in mydictionary.values())

# min and max methods 
print("\nMin and Max example:")

mynumist = [10,2,6,8,9,12,50]

print(min(mynumist))
print(max(mynumist))

# Random library: this library has tons of functions in it. To import any function, use the below syntax 
# from random import shuffle 
print("\nRandom library - shuffle example:")

mynewlist = [1,2,3,4,5,6,7,8,9,10]
# print(shuffle(mynumist))
 
# randint()
# print(randint(0,100)) # returns a random integer between 0 - 100 

# Saving user input in python : always accept te input as a "string", even the entered numbers are stringed. You can use 
# int(result) - to change the stringed number input value to an integer 
# (input('Please enter your name below'))

####  --- LIST COMPEREHENSIONS IN PYTHON --- #### 
# List comprehensions are a unique way of quickly creating a list with python. If you find yoursefl using for loop along with the 
# .append() to create a list. List comprehensions are a good alternative 
print("\nList Comprehensions example:")

myexample = 'gogodada'
newlist = []

for letter in myexample:
    newlist.append(letter)
print(newlist)
    
# Doing the same work as above using list comprehension

newlist = [letter for letter in myexample]
print(newlist)  # same result as above with less code 

anotherexample = [x for x in 'dorje']
print(anotherexample)

mylist = [num for num in range(0,10)] # first num is the what gets appended 
print(mylist)

mylist = [num + 2 for num in range(0,10)]
print(mylist)