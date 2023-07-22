# Definition for singly-linked list.
from typing import Optional
from math import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        num=0
        while p is not None:
            num+=1
            p=p.next
        index=0
        p=head
        while index != int(num/2):
            index+=1
            p=p.next
        return p
    
p=ListNode(1)
p.next=ListNode(2)
p.next.next=ListNode(3)
p.next.next.next=ListNode(4)
p.next.next.next.next=ListNode(5)

print(Solution().middleNode(p).val)