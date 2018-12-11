from collections import Counter

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def fib(n):
    cache_fib = {}
    cache_fib[0] = 0
    cache_fib[1] = 1

    for i in range(2, n+1):
        result = cache_fib[i-1] + cache_fib[i-2]
        cache_fib[i] = result

    return cache_fib[n]

def print_tree_node(root, depth):

    level = 1
    current_level = []
    current_level.append(root)

    while len(current_level):
        #if level == depth:
        print([v.value for v in current_level])
        #    return

        level += 1
        next_level = []
        for v in current_level:
            if v.left != None:
                next_level.append(v.left)
            if v.right != None:
                next_level.append(v.right)
        current_level = next_level


def reverse_tree(node):
    if node == None:
        return node

    tmp = node.left
    node.left = reverse_tree(node.right)
    node.right = reverse_tree(tmp)

    return node

def num_possible_move(target):

    if target == 0:
        return 0

    cache_possible_move = {}
    cache_possible_move[-4] = 0
    cache_possible_move[-3] = 0
    cache_possible_move[-2] = 0
    cache_possible_move[-1] = 0
    cache_possible_move[0] = 1
    cache_possible_move[1] = 1

    for i in range(2, target+1):
        result = cache_possible_move[i-1] + cache_possible_move[i-2] + \
                 cache_possible_move[i-3] + cache_possible_move[i-4] + \
                 cache_possible_move[i-5] + cache_possible_move[i-6]

        cache_possible_move[i] = result

    return cache_possible_move[target]


def count_words(string):
    words = string.split(" ")
    word_count = {}
    for w in words:
        word_count[w] = word_count.get(w, 0)
        word_count[w] += 1

    return word_count


if __name__ == '__main__':
    #print(fib(6))
    print(count_words('I am am having having'))
    print(num_possible_move(3))

    t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5, Node(6)), Node(8)))
    r = reverse_tree(t)
    print_tree_node(r, 3)
    print_tree_node(t, 3)