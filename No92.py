# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def toSet(self,root:Optional[TreeNode],s:Set[int]):
        if root is None:
            return s
        s.add(root.val)
        s=self.toSet(root.left,s)
        s=self.toSet(root.right,s)
        return s
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s=self.toSet(root,set())
        if len(s)<2:
            return -1
        s.remove(min(s))
        return min(s)
    
t=TreeNode(4)
t.left=TreeNode(1)
t.left.left=TreeNode(0)
t.left.right=TreeNode(2)
t.left.right.right=TreeNode(3)
t.right=TreeNode(6)
t.right.left=TreeNode(5)
t.right.right=TreeNode(7)
t.right.right.right=TreeNode(8)
print(Solution().findSecondMinimumValue(t))
        
