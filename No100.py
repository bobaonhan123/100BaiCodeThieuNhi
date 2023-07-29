from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def equal(self, r1:Optional[TreeNode],r2:Optional[TreeNode]):
        if r1 is None and r2 is None:
            return True
        if (r1 is None and r2 is not None) or (r1 is not None and r2 is None):
            return False
        if r1.val != r2.val:
            return False
        return self.equal(r1.left,r2.left) and self.equal(r1.right,r2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) or self.equal(root,subRoot)

r=TreeNode(3)
r.left=TreeNode(4)
r.right=TreeNode(5)
r.left.left=TreeNode(1)
r.left.right=TreeNode(2)
# r.left.right.left=TreeNode(0)

r2=TreeNode(4)
r2.left=TreeNode(1)
r2.right=TreeNode(2)

print(Solution().isSubtree(r,r2))
