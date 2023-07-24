# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def toList(self, root: Optional[TreeNode],li:List[int])->List[int]:
        if root is None:
            return li
        li=self.toList(root.left,li)
        li.append(root.val)
        li=self.toList(root.right,li)
        return li
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        li=self.toList(root,[])
        mi=abs(li[0]-li[1])
        for i in range(len(li)-1):
            mi=min(mi,abs(li[i]-li[i+1]))
        return mi
    
t=TreeNode(4)
t.left=TreeNode(1)
t.left.left=TreeNode(0)
t.left.right=TreeNode(2)
t.left.right.right=TreeNode(3)
t.right=TreeNode(6)
t.right.left=TreeNode(5)
t.right.right=TreeNode(7)
t.right.right.right=TreeNode(8)
print(Solution().getMinimumDifference(t))
