# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head is not None:
            p=ListNode(head.val)
            p.next=node
            node=p
            head=head.next
        return node
node=ListNode(0)
node.next=ListNode(1)
print(Solution().reverseList(node).val)