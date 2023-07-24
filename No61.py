# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if q is None and p is None:
            return True
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
p=TreeNode(1)
p.left=TreeNode(2)
p.right=TreeNode(3)

q=TreeNode(1)
q.left=TreeNode(2)
q.right=TreeNode(3)

print(Solution().isSameTree(p,q))