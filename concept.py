def outer_function():
    b = 20

    def inner_function():

        print('b =', b)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)


def pass_by_value(value):
    value = 2
    print(value)

value = 1
pass_by_value(value)
print(value)


list_to_be_sorted = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
new_list = sorted(list_to_be_sorted, key=lambda k: k['name'])

for item in new_list:
    print(item)


s = sorted(s, key = lambda x: (x[1], x[2]), reverse=True)
import operator
s = sorted(s, key = operator.itemgetter(1, 2), reverse=True)

'''
Creating empty Dictionary
'''
# Creating an empty dict using empty brackets
wordFrequency = {}
# Creating an empty dict using dict()
wordFrequency = dict()

# List of tuples
listofTuples = [("Hello" , 7), ("hi" , 10), ("there" , 45),("at" , 23),("this" , 77)]
# Creating and initializing a dict by tuple
wordFrequency = dict(listofTuples)


listofStrings = ["Hello", "hi", "there", "at", "this"]
wordFrequency = dict.fromkeys(listofStrings,0 )


# List of strings
listofStrings = ["Hello", "hi", "there", "at", "this"]
# List of ints
listofInts = [7, 10, 45, 23, 77]
# Merge the two lists to create a dictionary
wordFrequency = dict( zip(listofStrings,listofInts ))

# merge two dicts
z = {**x, **y}


# Asterisks for unpacking into function call
# When calling a function, the * operator can be used to unpack an iterable into the arguments in the function call:

>>> fruits = ['lemon', 'pear', 'watermelon', 'tomato']
>>> print(fruits[0], fruits[1], fruits[2], fruits[3])
lemon pear watermelon tomato
>>> print(*fruits)
lemon pear watermelon tomato

