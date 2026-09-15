
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        # Your code goes here
        if head.next==None:
            return None
        curr=head.next
        head.next=None
        curr.prev=None
        head=curr
        return head