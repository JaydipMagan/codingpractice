# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        def dfs(node,list_so_far):
            # Check leaf
            if node.left==None and node.right==None:
                if arr==list_so_far:
                    return True
            else:
                l = dfs(node.left,list_so_far+[node.left.val]) if node.left!=None else False            
                r = dfs(node.right,list_so_far+[node.right.val]) if node.right!=None else False
                return l or r
        return dfs(root,[root.val])
