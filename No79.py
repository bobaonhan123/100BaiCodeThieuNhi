# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.height(root.left)+self.height(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
    

t=TreeNode(4)
t.left=TreeNode(1)
t.left.left=TreeNode(0)
t.left.right=TreeNode(2)
t.left.right.right=TreeNode(3)
t.right=TreeNode(6)
t.right.left=TreeNode(5)
t.right.right=TreeNode(7)
t.right.right.right=TreeNode(8)

print(Solution().diameterOfBinaryTree(t))