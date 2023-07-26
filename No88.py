# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, nums: List[int], node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        r=len(nums)-1
        l=0
        m=(r+l)//2
        node = TreeNode(nums[m])
        node.left=self.solve(nums[l:m],node.left)
        node.right=self.solve(nums[m+1:r+1],node.right)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.solve(nums,None)
        

        
a=Solution().sortedArrayToBST([1,2,3,4])
print(a.left.val,a.right.val)