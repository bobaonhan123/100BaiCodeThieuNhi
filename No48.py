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
    def recursion(self,root:Optional[TreeNode],k:int) -> int:
        if root is None:
            return k
        k=self.recursion(root.right,k)
        root.val=root.val+k
        k=self.recursion(root.left,root.val)
        return k
    
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        t=self.recursion(root,0)
        return root
t=TreeNode(4)
t.left=TreeNode(1)
t.left.left=TreeNode(0)
t.left.right=TreeNode(2)
t.left.right.right=TreeNode(3)
t.right=TreeNode(6)
t.right.left=TreeNode(5)
t.right.right=TreeNode(7)
t.right.right.right=TreeNode(8)

print(Solution().tree2str(Solution().convertBST(t)))