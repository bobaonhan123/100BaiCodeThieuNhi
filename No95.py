# Definition for a binary tree node.
from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self,root:Optional[TreeNode],li:List[int],rank)->List[int]:
        if root is None:
            return li
        if rank==len(li):
            li.append([])
        li[rank].append(root.val)
        li=self.dfs(root.left,li,rank+1)
        li=self.dfs(root.right,li,rank+1)
        return li
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        li=self.dfs(root,[],0)
        return li[::-1]
        
t=TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
t.right.left=TreeNode(15)
t.right.right=TreeNode(7)
print(Solution().levelOrderBottom(t))