# Sample solution
#  def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         max_path = 0
        
#         def traverse(root):
#             nonlocal max_path
#             if not root:
#                 return 0
            
#             left = traverse(root.left)
#             right = traverse(root.right)
            
#             curr_path = left + right
#             if curr_path > max_path:
#                 max_path = curr_path
            
#             return max(left, right) + 1
        
#         max_path = 0
#         traverse(root)
#         return max_path


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self,node) -> bool:
        if node.left==None and node.right==None:
            return True
        return False

# My paintful attempt
#     def dfs(self, root):
#         if root==None:
#             return [],[0],[]
#         stack = [root]
#         visited = []
#         edges = [0]
#         nodes = []
#         while stack!=[]:
#             node = stack.pop()
#             visited.append(node.val)
#             if self.isLeaf(node):
#                 edges.append(edges[-1]-1)
#             edges.append(edges[-1]+1)
#             if node.right!=None:
#                 stack.append(node.right)
#                 nodes.append(1)
#             if node.left!=None:
#                 stack.append(node.left)
#                 nodes.append(0)
#         return (visited,edges[:-1],nodes)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node): 
            # Base Case : Tree is empty 
            if node is None: 
                return 0 ; 

            # If tree is not empty then height = 1 + max of left  
            # height and right heights  
            return 1 + max(height(node.left) ,height(node.right)) 
        
        # Function to get the diamtere of a binary tree 
        def diameter(root): 

            # Base Case when tree is empty  
            if root is None: 
                return 0; 

            # Get the height of left and right sub-trees 
            lheight = height(root.left) 
            rheight = height(root.right) 

            # Get the diameter of left and irgh sub-trees 
            ldiameter = diameter(root.left) 
            rdiameter = diameter(root.right) 

            # Return max of the following tree: 
            # 1) Diameter of left subtree 
            # 2) Diameter of right subtree 
            # 3) Height of left subtree + height of right subtree +1  
            return max(lheight + rheight , max(ldiameter, rdiameter)) 
        return diameter(root)
