# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        return_node = head
        size = 1
        while head.next!=None:
            size+=1
            head = head.next
        
        point = (size/2) if (size%2==0) else int((size/2))

        while point>0:
            return_node = return_node.next
            point-=1
        return return_node

