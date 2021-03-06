import sys
import math
import copy
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

'''
m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive
l0 = input()  # L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
l1 = input()
l2 = input()
l3 = input()
'''

m = 1
v = 1
l0 = '...0......'
l1 = '...00.....'
l2 = '...0..0...'
l3 = '...0......'

l0 = '..............................'
l1 = '..............................'
l2 = '...........0..................'
l3 = '..............................'

l0 = '.............................0..0....'
l1 = '.0.0..................000....000.....'
l2 = '....000.........0.0...000............'
l3 = '............0.0......................'

def to_np_array(lines):
    lane = ()
    for line in lines:
        line = ",".join(line.replace('.', '1'))
        line = [int(val) for val in line.split(',')]
        lane += (line,)
    return np.array(lane)


board = to_np_array([l0, l1, l2, l3])

SPEED = 'SPEED'
SLOW = 'SLOW'
JUMP = 'JUMP'
WAIT = 'WAIT'
UP = 'UP'
DOWN = 'DOWN'

possible_commands = [UP, SPEED, JUMP, DOWN, WAIT, SLOW]

max_speed = 10
max_depth = 5
min_num_suvive = v

class Bike:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.speed = s


# check after the command, if a bike is still alive
def is_safe(command, bike, board):

    new_speed = bike.speed
    new_x = bike.x
    new_y = bike.y

    if command == SPEED:
        new_speed += 1
    elif command == SLOW:
        new_speed -= 1
    elif command == UP:
        new_y -= 1
    elif command == DOWN:
        new_y += 1

    new_x += new_speed

    # cap the x coordinate
    new_x = min(board.shape[1]-1, new_x)

    if command == UP or command == DOWN:
        # check next lane
        num_holes = np.sum(board[new_y][bike.x + 1: new_x + 1] == 0)

        # check original lane
        if new_x > bike.x + 1:
            num_holes += np.sum(board[bike.y][bike.x + 1: new_x] == 0)

    elif command != JUMP:
        num_holes = np.sum(board[new_y][bike.x: new_x + 1] == 0)
    elif command == JUMP:
        num_holes = not board[new_y][new_x]

    if num_holes:
        return False

    bike.x = new_x
    bike.y = new_y
    bike.speed = new_speed
    return True

# check if COMMAND is a valid candidate
# based on current state of the bike
# equ. to player strategy

def is_valid_command(command, bikes):

    # dun want to go too fast
    if bikes[0].speed >= max_speed and command == SPEED:
        return False

    # bike has 0 speed
    if bikes[0].speed == 0 and command != SPEED:
        return False

    if bikes[0].speed == 1 and command == SLOW:
        return False

    max_y = max(bike.y for bike in bikes)
    if max_y == 3 and command == UP:
        return False

    min_y = min(bike.y for bike in bikes)
    if min_y == 0 and command == DOWN:
        return False

    return True


def execute_command(command, bikes, board):
    num_safes = 0

    alive_bikes = []
    for bike in bikes:
        if is_safe(command, bike, board):
            alive_bikes.append(bike)
            num_safes += 1

    return num_safes, alive_bikes

def find_solution(command, bikes, board, sol, depth):

    if depth > max_depth:
        return True

    if(is_valid_command(command, bikes)):
        num_safes, alive_bikes = execute_command(command, copy.deepcopy(bikes), board)
        if num_safes < min_num_suvive:
            return False
        else:
            sol.append((command, num_safes))

            # consider next command
            for next_command in possible_commands:
                if(find_solution(next_command, alive_bikes, board, sol, depth+1)):
                    return True

            # if none of the above commands work then
            # BACKTRACK: remove command from solution
            sol.pop()
            return False

    return False

def find_local_optimal(bikes, board):
    solutions = {}
    for command in possible_commands:
        sol = []
        if find_solution(command, bikes, board, sol, 1):
            num_survive = sol[-1][1]

            if solutions.get(num_survive, None) is None:
                solutions[num_survive] = sol

            if num_survive == m:
                break

    best_num_survive = max(solutions.keys())
    return solutions[best_num_survive]

rounds = 2
current_round = 0

# game loop
while True:
    #s = int(input())  # the motorbikes' speed
    s = 4

    bikes = []
    for i in range(m):
        # x: x coordinate of the motorbike
        # y: y coordinate of the motorbike
        # a: indicates whether the motorbike is activated "1" or detroyed "0"
        #x, y, a = [int(j) for j in input().split()]

        x, y, a = [0, 2, 1]

        if a:
            bike = Bike(x, y, s)
            bikes.append(bike)

    if current_round % rounds == 0:
        solutions = find_local_optimal(bikes, board)

    current_round += 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # A single line containing one of 6 keywords: SPEED, SLOW, JUMP, WAIT, UP, DOWN.
    print(solutions.pop(0))