#!/usr/bin/py
def printStaircase(levels):
    for i in range(1, levels + 1):
        print(("#" * i).rjust(levels))


if __name__ == '__main__':
    t = int(input())
    printStaircase(t)