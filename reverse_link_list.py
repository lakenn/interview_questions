class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return '%s' % self.value


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

start = ptr = n1


def reverse(node, prev):
    if node is None:
        node =  Node(-1)
        node.next = prev
        return node

    next = node.next
    node.next = prev

    return reverse(next, node)

reverse_node = reverse(n1, None)
print(1)






