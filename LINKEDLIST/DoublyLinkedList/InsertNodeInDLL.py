#  Structure of Doubly Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        pos=0
        curr=head
        while curr!=None:
            if pos==p:
                newNode=Node(x)
                newNode.prev=curr
                newNode.next=curr.next
                curr.next=newNode
                if newNode.next:
                    newNode.next.prev=newNode
                else:
                    newNode.next=None
            curr=curr.next
            pos=pos+1
        return head