# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head==None:
            return head
        temp=None
        curr=head
        while curr:
            front=curr.next
            curr.next=temp
            temp=curr
            curr=front
            
        return temp