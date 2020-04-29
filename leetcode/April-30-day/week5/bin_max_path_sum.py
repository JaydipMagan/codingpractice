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