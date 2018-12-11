class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.method)
print(MyClass.method)
print(obj.classmethod())

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'


Pizza(['cheese', 'tomatoes'])

def append(number, number_list=[]):
    number_list.append(number)
    print(number_list)
    return number_list

append(5)
append(7)

append(8, [1,2])
append(9)