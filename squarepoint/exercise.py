import threading
import re

def find_all_occurrence(s, substr):
    for match in re.finditer(substr, s):
        yield match


for match in find_all_occurrence("appple apple apple2", 'pp'):
    print(match.start())

def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")