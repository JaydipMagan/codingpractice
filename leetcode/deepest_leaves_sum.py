# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        
        def dfs(node):
            if node==None:
                return 0
            if node.left!=None and node.right!=None:
                return max(1+dfs(node.left),1+dfs(node.right))
            elif node.left==None and node.right==None:
                return 0
            elif node.left==None and node.right!=None:
                return 1+dfs(node.right)
            else:
                return 1+dfs(node.left)
            
        def findDeepestLeaves(current,target,node,leafs):
            if current==target and node!=None:
                return leafs.append(node.val)
            x , y = None, None
            if node.left!=None and node.right!=None:
                x = findDeepestLeaves(current+1,target,node.left,leafs)
                y = findDeepestLeaves(current+1,target,node.right,leafs)
            elif node.left!=None and node.right==None:
                x = findDeepestLeaves(current+1,target,node.left,leafs)
            elif node.left==None and node.right!=None:
                x = findDeepestLeaves(current+1,target,node.right,leafs)
            else:
                return None
            if x!=None:
                leafs+[x]
            if y!=None:
                leafs+[x]
            return leafs
                
            
        x = dfs(root)
        # print(x)
        nodes = findDeepestLeaves(0,x,root,[])
        # print(nodes)
        nodes_sum = sum(nodes)
        return nodes_sum
                