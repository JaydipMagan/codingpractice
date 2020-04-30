"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]


Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.

"""
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