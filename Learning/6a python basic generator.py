def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield 0
    return sub_generator()  # Calls another generator
    yield 4

# Using the main generator
for value in main_generator():
    print(value)
