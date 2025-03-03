
def manyArgs(*arg):
  print("I was called with", len(arg), "arguments:", arg)

manyArgs(1)
manyArgs(1, 2, 3)


a = [1, 2, 3]
b = ['a', 'b', 'c']

zipped = zip(a, b)

x = 1
def greet(name):
  # inner function
  x = 2
  def display_name():
    nonlocal x
    x= 3
    print("Hi", x)

  # call inner function
  display_name()
  print(x)

# call outer function
greet("John")
print(x)
# Output: Hi John