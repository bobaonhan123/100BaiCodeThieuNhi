
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            root1.left=self.mergeTrees(root1.left,root2.left)
            root1.right=self.mergeTrees(root1.right,root2.right)
            root1.val+=root2.val
        return root1

t1=[1,3,2,5]
t2=[2,1,3,None,4,None,7]

tree1=TreeNode(1)
tree1.left=TreeNode(3)
tree1.right=TreeNode(2)
tree1.left.left=TreeNode(5)

tree2=TreeNode(2)
tree2.left=TreeNode(1)
tree2.right=TreeNode(3)
tree2.left.right=TreeNode(4)
tree2.right.right=TreeNode(7)

print(Solution().mergeTrees(tree1,tree2).val)