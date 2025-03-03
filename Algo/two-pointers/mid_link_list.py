import threading


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
