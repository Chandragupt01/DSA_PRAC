"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    def insertAtFront(self, head, x):
        #code here
        curr=Node(x)
        curr.next=head
        head=curr
        
        return head
