####  --- STRINGS IN PYTHON --- #### 
# Strings can be indexed 
word = 'Python'
word[0]  # character in position 0 --> 'P'
word[5]  # character in position 5--> 'n'

# Indices may also be negative numbers, to start counting from the right:
word[-1]  # last character --> 'n'
word[-2]  # second-last character -> 'o'
word[-6] # selects first character --> 'P'

# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
word[0:2]  # characters from position 0 (included) to 2 (excluded) --> 'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded) --> 'tho'

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
word[:2]   # character from the beginning to position 2 (excluded) --> 'Py'
word[4:]   # characters from position 4 (included) to the end --> 'on'
word[-2:]  # characters from the second-last (included) to the end --> 'on'


####  --- DICTIONARIES IN PYTHON --- #### 
person = {'name':'Dorje', 'age': 28, 'city':'Richmond', 'state':'California'}
print(person)
name_is = person['name']
print(name_is)
print(person['age'])
print(person['city'])

# Getting all the keys or values from a dictionary 
print(person.keys())
print(person.values())

# Getting both the keys and the value together 
print(person.items())

# dictionary with list as a value
car = {'model': 'T3', 'color':['red', 'yellow', 'green'], 'year':2020}
print(car['model'])
print(car['color'][1])

alpha = {'letters': ['a','b','c']}
print(alpha['letters'][1].upper())

numbs = {'a': 100, 'b':200, 'c':300}
numbs['d'] = 400  # adds 'd':400 to the numbs dictionary 
print(numbs)
numbs['new_value'] = 'yep'
print(numbs)

# Getting all the keys or values from a dictionary 
print(numbs.keys())
print(numbs.values())

# Getting both the keys and the value together 
print(numbs.items())


####  --- TUPLES IN PYTHON --- #### 
# Tuples are very similar to Lists. However, they have one difference - tuples are IMMUTABLE ( can't be changed ). It basically means once an element is assigned to an index position inside a tuple, you can't grab that element and reassigned another value. 
# Tuples looks like Lists, except it uses ( )
t = ('one', 2, 'three', 4.5)
print(t[1])
print(t[-1]) # prints 4.5 because we are getting the element at last index by using the -1 

# 2 built-in methods for Tuple - index() and count() methods 
# Count():
name = ('dorje', 'dorje', 'damdul', 1, 3, 3, 5, 3)
print(name.count('dorje'))
print(name.count(3))


####  --- SETS IN PYTHON --- #### 
# Sets are unordered collection of unique elements - meaning there can only be one representative of the same object 
myset = set()
myset.add(1)
myset.add(2)
print(myset)
myset.add(2)
print(myset) # this will not add another 2 to the set, because set only can contain unique element - meaning can't have same value twice 


####  --- BOOLEANS IN PYTHON --- #### 
# Booleans are operators that allow you to convey True or False statements. In python its 'True' and 'False' 
print(1 == 1)
print(100 < 50)

b = None
print(type(b))


# I/O Basics of Files in Python 
# muffle.read() --> outputs a giant string of everything in the file 
# # .readlines() --> outputs each sentence as a list 

# Opening a file living somewhere on your computer, just pass in the file path
# .open('...file - path..')
# should use forward slash '/' in the file path 
# Always make sure to close the file once done with it by .close()