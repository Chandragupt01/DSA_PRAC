''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        len=0
        curr=head
        if head==None:
            return len
        while curr:
            len+=1
            curr=curr.next
            
        return len