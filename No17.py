from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root is not None:
            root.left=self.trimBST(root.left,low,high)
            root.right=self.trimBST(root.right,low,high)
        while root is not None and (root.val<low or root.val>high):
            if root.left is not None and root.left.val>=low and root.left.val<=high:
                root=root.left
            else:
                root=root.right
        
        return root

root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)
print(Solution().trimBST(root,3,4) is None)