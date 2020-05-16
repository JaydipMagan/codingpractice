"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        def getInfo(node):
            n = 0
            end = None
            while node:
                n+=1                
                end = node
                node = node.next
            return n,end
    
        n,end = getInfo(head)
        temp = head
        while n>1:
            if head and head.next:
                end.next = temp.next
                end = end.next
                
                temp.next = temp.next.next
                temp = temp.next
                end.next = None
                n-=2
        return head
    