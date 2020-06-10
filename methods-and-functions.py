# METHODS:
# Build in methods:
print("\nBuilt-in Methods example:")

mylist = [1,2,3,4]
mylist.append('five')
print(mylist)

mylist.pop(0)
print(mylist)

mylist.insert(0, 'one')
print(mylist)

# FUNCTIONS: 
print("\nFunction example:")

def num_adder(a, b):
    '''
    You can comment here, within the quotes
    This function adds 2 numbers
    '''
    added = a + b
    print(added)

num_adder(2, 2)

# Say Hello: using default value for name param, if no value for name is supplied then it will use that default value 
def say_hello(name = "Phuntsok"):
    print("Hello " + name)

say_hello() # prints "Hello Phuntsok" 
say_hello("Dorje")

# Celcius to Degree convertor: 
def cel_to_degree(cel):
    return ((cel * 9/5) + 32)

result = cel_to_degree(10)
print(result)

# return in function:
def add(n1, n2):
    return n1 + n2

result = add(20, 20)
print(result)

# Color checker:
def color_check(color):
    return 'pink' in color.lower()

result = color_check('Red Green Pink Yellow')
print(result)

# PIG LATIN exercise:
# if the word starts with a vowel, add 'ay' to the end
# if the word doesn't start with a vowel, put the first letter at the end of the word and then add 'ay'
def pig_latin_translator(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay' # word from index 1 all the way to the end 

result = pig_latin_translator('ooo')
print(result)

# print(sum((2, 2)))

# write me a song function:


# *args = arbitrary number of arguments, returns a tuple 
# **kwargs (key word arguments): builds or returns a dictionary of key - value pairs 

print("\n*args example:")
def myfunc(*args):
    # print(args)
    result = sum(args) * 0.05
    # return sum(args) - result is same as above 
    print(result)

myfunc(40,60,100)

print("\n**kwargs example:")
def fruitfinder(**kwargs):
    # print(kwargs)
    if 'fruit' in kwargs:
        print('My favorite choice of fruit is {}.'.format(kwargs['fruit']))
    else:
        print('No fruit is found here!')

fruitfinder(fruit = 'apple', veggie = 'kale')

print("\n*args and **kwargs combination example:")
def combo(*args, **kwargs):
    # print(args) -> prints (10, 250, 12)
    # print(kwargs) -> prints {'fruit': 'coconuts', 'food': 'fruits', 'animal': 'cat'}
    print('I would like {} {}'.format(args[1], kwargs['fruit']))

combo(10,250, 12, fruit = 'coconuts', food = 'fruits', animal = 'cat')

#Defines a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those that are even 
def myfunca(*args):
    return [x for x in args if x % 2 == 0]

### LAMBDA EXPRESSIONS, MAP AND FILTER FUNCTIONS: ### 
## MAP ##
print("\nLambda, Map and Filter Examples:")

# example 1 :  map applies square function to every element in the my_nums list
print("\nMapExamples:")

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)
# or 
print(list(map(square, my_nums))) # prints result in a list 

# example 2: map applies splicer function to every element in the my_names list 
def splicer(stg):
    if len(stg) % 2 == 0:
        return "EVEN"
    else:
        return stg[0]

my_names = ['Gogo', 'Jalayla', 'Pappu', 'Gaggu', 'Raka']

evennames = list(map(splicer, my_names))
print(evennames)

## FILTER: filters based off of the condition mentioned in the function ##
print("\nFilter Examples:")

def check_even(num):
    return num % 2 == 0

my_nums = [1,2,3,4,5,6,7,8,9,10]

for num in filter(check_even, my_nums):
    print(num)

# or 
my_new_list = list(filter(check_even, my_nums))

print(my_new_list)

## LAMBDA EXPRESSION - a.k.a Anonymous function, ##
print("\nLambda Examples:")

print(list(map(lambda num:num % 2 == 0, my_nums)))

print(list(map(lambda name:name[0].lower(), my_names)))

print(list(map(lambda name:name[::-1], my_names)))


## NESTED STATEMENTS AND SCOPES  ##
print("\nNested Statements and Scopes Examples:")
# LEGB Rule:
# L: Local - Names assigned in any way within a function (def or lambda), and NOT declared global in that function 
# E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer 
# G : Global (module) - Names assigned at the top level of a module-file, or declared global in a def within a file 
# B: Built-in (Python) - Names preassigned in the built-in names modules: open, range, SyntaxError etc 
# example:
name = "Global name!"

def greeting():

    #Enclosing
    name = "Enclosing name!"

    def say_hello():
        #Local
        # name = "Local name!"
        print('Hello ' + name)

    say_hello()

greeting()

#this is called f-string notation:  print(f'some string goes here')
x = 5
def func(x):
    print(f'Value of first X is {x}')

    # Local reassignment 
    x = 200
    print(f'Value of X is changed to new X value {x}')

func(x)