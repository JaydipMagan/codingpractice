"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        bottom_up = collections.defaultdict(list)
        
        def dfs(root,level):
            
            if root:
                if bottom_up[level]:
                    l = bottom_up[level]
                    l.append(root.val)
                    bottom_up[level] = l
                else:
                    bottom_up[level] = [root.val]
                left = dfs(root.left,level+1)
                right = dfs(root.right,level+1)
                
        dfs(root,0)
        out = list(bottom_up.values())
        return out[::-1]