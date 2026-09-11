'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        currNode=head
        if currNode==None:
            return Node(x)
        while currNode.next!=None:
            currNode=currNode.next
        
        newEle=Node(x)
        currNode.next=newEle
    
        return head            