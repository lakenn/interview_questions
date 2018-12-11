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