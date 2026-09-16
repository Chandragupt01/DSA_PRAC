""" Structure of a Doubly Linked List Node
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        # code here
        pos=1
        curr=head
        while curr!=None:
            if pos==x:
                if curr==None:
                    return head
                if curr.prev:
                    curr.prev.next=curr.next
                if curr.next:
                    curr.next.prev=curr.prev
                if curr==head:
                    head=curr.next
                    head.prev=None
                    curr.next=None
                    curr.prev=None
            curr=curr.next
            pos+=1
            
        return head