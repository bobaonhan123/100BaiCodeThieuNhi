# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findNode(self, root: Optional[TreeNode], k: int) ->bool:
        if root is None:
            return False
        if root.val==k:
            return True
        if root.val<k:
            return self.findNode(root.right,k)
        return self.findNode(root.left,k)
    def check(self, root: Optional[TreeNode],node:Optional[TreeNode], k: int)->bool:
        if node is None:
            return False
        return (self.findNode(root,k-node.val) if k%2!=0 or k//2!=node.val else 0) or self.check(root,node.left,k) or self.check(root,node.right,k)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.check(root,root,k)

t=TreeNode(5)
t.left=TreeNode(3)
t.right=TreeNode(6)
t.left.left=TreeNode(2)
t.left.right=TreeNode(4)
t.right.right=TreeNode(7)

print(Solution().findTarget(t,9))