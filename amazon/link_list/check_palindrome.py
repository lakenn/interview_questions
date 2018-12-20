class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return '%s' % self.value


n1 = Node('R')
n2 = Node('A')
n3 = Node('D')
n4 = Node('A')
n5 = Node('R')

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

def check_palindrome(head):

    stack = []

    current = head
    while current:
        stack.append(current.value)
        current = current.next


    current = head
    while current:

        letter = stack.pop(-1)
        if current.value != letter:
            return False

        current = current.next

    return True

print(check_palindrome(head))







