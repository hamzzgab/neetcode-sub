# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        ptr1, ptr2 = list1, list2
        node = ListNode()
        head = node
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                node.next = ptr1
                ptr1 = ptr1.next
            else:
                node.next = ptr2
                ptr2 = ptr2.next
            node = node.next  

        while ptr1:
            node.next = ptr1
            ptr1 = ptr1.next
            node = node.next
        
        while ptr2:
            node.next = ptr2
            ptr2 = ptr2.next
            node = node.next

        return head.next
                
