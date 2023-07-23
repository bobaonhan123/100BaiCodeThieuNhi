# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.left is None and root.right is not None:
            return str(root.val)+"()"+"("+self.tree2str(root.right)+")"
        if root.left is not None and root.right is None:
            return str(root.val)+"("+self.tree2str(root.left)+")"
        return str(root.val)+"("+self.tree2str(root.left)+")"+"("+self.tree2str(root.right)+")"
    
t=TreeNode(1)
t.left=TreeNode(2)
t.left.right=TreeNode(4)
t.right=TreeNode(3)
print(Solution().tree2str(t))