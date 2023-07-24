# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursion(self,root:Optional[TreeNode],state:bool)->int:
        if root is None:
            return 0
        if state:
            if root.left is None and root.right is None:
                return root.val
        return self.recursion(root.left,True)+self.recursion(root.right,False)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root,False)
    
t=TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
t.right.left=TreeNode(15)
t.right.right=TreeNode(7)

print(Solution().sumOfLeftLeaves(t))