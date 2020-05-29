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



