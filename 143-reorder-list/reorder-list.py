# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1) get to the middle of the list 
        2) reverse the back half 
        3) merge both of the half lists together 
        """
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        curr = slow.next
        slow.next = None 
        prev,temp = None, None
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        """
        create a temp head to return 
        head.next = prev
        prev.next = where head.next would have been 
        head = where head.next would have been 
        prev = where prev.next would have been
        """
        temp_head = head
        while head and prev:
            first_next_stored = head.next 
            second_next_stored = prev.next
            
            head.next = prev
            prev.next = first_next_stored
            head = first_next_stored
            prev = second_next_stored
        
        return temp_head

        