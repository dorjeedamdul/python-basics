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




