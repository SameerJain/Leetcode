# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Curr1
1  -> 2   -> 4



Curr2
2->   3   ->  4

1->1->2->3->4->4


iterate thru both lists

if one value is less
    set that as the next node
    set temp.next = curr

if one list hasnt been passed thru
    add everything thats left
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
            
        curr1 = list1
        curr2 = list2

        new_head = None

        if curr1.val < curr2.val:
            new_head = curr1
            curr1 = curr1.next
        else:
            new_head = curr2
            curr2 = curr2.next

        temp = new_head

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next
        
        while curr1:
            temp.next = curr1
            curr1 = curr1.next
            temp = temp.next
        
        while curr2:
            temp.next = curr2
            curr2 = curr2.next
            temp = temp.next
        
        return new_head
        



        