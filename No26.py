# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursion(self,root:Optional[TreeNode],level:int,li:List[List[int]]) -> List[List[int]]:
        if root is None:
            return li
        if(len(li)==level):
            li.append([])
        li[level].append(root.val)
        li=self.recursion(root.left,level+1,li)
        li=self.recursion(root.right,level+1,li)
        return li
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        li=self.recursion(root,0,[])
        res=[]
        for i in li:
            su=0
            for j in i:
                su+=j
            res.append(su/len(i))
        return res
    
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

print(Solution().averageOfLevels(root))
