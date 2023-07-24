# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next

t=ListNode(1)
node=ListNode(2)
t.next=node
node.next=ListNode(3)
Solution().deleteNode(node)
print(t.val,t.next.val)