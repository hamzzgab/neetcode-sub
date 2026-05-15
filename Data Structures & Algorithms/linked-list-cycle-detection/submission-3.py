# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tur, har = head, head

        while har and har.next:
            tur = tur.next
            har = har.next.next
            if tur == har:
                return True
        return False