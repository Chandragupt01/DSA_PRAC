''' Linked List Node Structure
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
from typing import List
class Solution:
    def arrayToList(self, arr: List[int]) -> 'Node':
        # code here
        n=len(arr)
        newHead=Node(arr[0])
        currnode=newHead
        for i in range(1,n):
            newnode=Node(arr[i])
            currnode.next=newnode
            currnode=newnode
        return newHead
        