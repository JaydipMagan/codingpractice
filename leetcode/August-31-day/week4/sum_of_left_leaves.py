"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(root,left):
            if not root:return
            
            if not root.left and not root.right:
                if left==True:self.sum_left_leafs+=root.val
            
            dfs(root.left,True)
            dfs(root.right,False)
        self.sum_left_leafs = 0    
        dfs(root,False)
        return self.sum_left_leafs