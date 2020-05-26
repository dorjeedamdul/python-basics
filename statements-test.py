# 1. Use for, .split(), and if to create a Statement that will print out words that start with 's':
print('\nAnswer 1')
st = 'Print only the words that start with s in this sentence'

newst = st.split()
print(newst)

for words in newst:
    if words[0] == 's':
        print(words)

# 2. Use range() to print all the even numbers from 0 to 10
print('\nAnswer 2')
print(list(range(0,11)))


# 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
print('\nAnswer 3')
mynum = [x for x in range(1,51) if x % 3 == 0]
print(mynum)

# 4. Go through the string below and if the length of a word is even print "even!"
print('\nAnswer 4')

st = 'Print every word in this sentence that has an even number of letters'
newst = st.split()

for letters in newst:
    if len(letters) % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
print('\nAnswer 4')

for numba in range(1, 100):
    if numba % 3 == 0 and numba % 5 == 0:
        print("FizzBuzz")
    elif numba % 3 == 0:
        print("Fizz")
    elif numba % 5 == 0:
        print("FizzBuzz")
    else:
        print(f'{numba} is not divisible by 3 or 5!')

# 6. Use List Comprehension to create a list of the first letters of every word in the string below:
print('\nAnswer 6')

st = 'Create a list of the first letters of every word in this string'
new_list = [x[0] for x in st.split()]
print(new_list)

print('\nAnswer 6 - second version:')

new_st = st.split()
new_list = [x[0] for x in new_st]
print(new_list)
