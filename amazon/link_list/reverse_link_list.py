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

head = n1

def reverse(head):

    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    head = prev

    return head

reverse_node = reverse(head)
print(1)






