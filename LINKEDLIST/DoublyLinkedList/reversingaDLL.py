""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        curr=head
        temp=None
        while curr:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
            if temp is not None:
                    head = temp.prev

        return head