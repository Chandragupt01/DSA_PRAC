class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def createDLL(self, arr):
       # code here
     n=len(arr)
     head=Node(arr[0])
     curr=head
     for i in range(1,n):
        newNode=Node(arr[i])
        newNode.prev=curr
        curr.next=newNode
        curr=newNode
     return head