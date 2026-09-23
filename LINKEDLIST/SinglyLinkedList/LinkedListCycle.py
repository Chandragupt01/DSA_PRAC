# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#optimal
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False

#Brute Force
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited=set()
#         temp=head
#         while temp!=None:
#             if temp in visited:
#                 return True
#             visited.add(temp)
#             temp=temp.next
#         return False