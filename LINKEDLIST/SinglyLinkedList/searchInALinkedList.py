'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        # Code here
        curr=head
        flag=False
        while curr:
            if curr.data==key:
                flag=True
            curr=curr.next
        return flag