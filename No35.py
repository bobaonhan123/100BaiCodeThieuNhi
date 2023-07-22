# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        right=self.invertTree(root.left)
        left=self.invertTree(root.right)
        root.right=right
        root.left=left
        return root
root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)
print(Solution().invertTree(root).left.val)