# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def insert(self, node, i):
#         # print(node, i)
#         if node is None:
#             node = TreeNode(i)
#         elif node.val > i:
#             node.left = self.insert(node.left, i)
#         elif node.val < i:
#             node.right = self.insert(node.right, i)
#         return node
    
#     def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#         root = TreeNode(preorder[0])
#         node = root
#         for i in preorder[1:]:
#             self.insert(root, i)
#         return root
    # def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
            
    #         if not preorder:
    #             return None
            
    #         first = preorder.pop(0)
    #         node = TreeNode(first)
            
    #         i = 0
    #         n = len(preorder)
    #         while i < n and preorder[i] < first:
    #             i += 1
                
    #         node.left = self.bstFromPreorder(preorder[:i])
    #         node.right = self.bstFromPreorder(preorder[i:])
            
    #         return node
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        
        def make_tree(node,vals):
            
            new_left = [x for x in vals if x<node.val]
            new_right = [x for x in vals if x>node.val]
            
            if len(new_left)==0 and len(new_right)==0: # leaf node
                return node
            
            elif len(new_left)!=0 and len(new_right)==0: # no right subtree
                left_node = make_tree(TreeNode(new_left[0]),new_left)   
                node.left = left_node
            elif len(new_left)==0 and len(new_right)!=0: # no right subtree
                right_node = make_tree(TreeNode(new_right[0]),new_right)         
                node.right = right_node
            else:
                left_node = make_tree(TreeNode(new_left[0]),new_left)        
                right_node = make_tree(TreeNode(new_right[0]),new_right)         
                node.left = left_node
                node.right = right_node
            return node
            
                
        
        root = TreeNode(preorder[0])
        final = make_tree(root,preorder)
        
        
        return final