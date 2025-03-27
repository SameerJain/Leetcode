# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
inititialize a fast and a slow pointer
loop for as long as there are 2 nodes left in the list 
fast pointer moves by 2, slow moves by 1
if theres a cycle, eventually they will match up 
if theres no cycle, they will terminate and the loop stops 

in the case that the fast node reaches the second to last node:
if there is a cycle then eventually we will return true, but if there is no cycle then it 
doesnt matter that the last node will never be evaluated. theres still no cycle.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_node = head
        fast_node = head
        
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                return True
        return False