"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    current_max = float('-inf')
    def max_sum(self,node):
        if node==None:
            return 0
        
        n = node.val
        l = self.max_sum(node.left)
        r = self.max_sum(node.right)
            
        max_subtree = max(l,r)
        max_parent_child = max(max_subtree+n,n)
        whole = max(max_parent_child,l+r+n)
        self.current_max = max(self.current_max,whole)
        
        return max_parent_child
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        x = self.max_sum(root)
        print(self.current_max)
        return self.current_max