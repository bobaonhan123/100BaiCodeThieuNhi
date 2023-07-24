# Definition for a binary tree node.
from typing import Optional
from math import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def total(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return root.val+self.total(root.left)+self.total(root.right)
    def recursion(self, root: Optional[TreeNode]) -> int:
        root.val=abs(self.total(root.left)-self.total(root.right))
        if root.left is not None:
            root.left.val=self.recursion(root.left)
        if root.right is not None:
            root.right.val=self.recursion(root.right)
        return root.val
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        root.val=self.recursion(root)
        return self.total(root)
        
    
t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
print(Solution().findTilt(t))