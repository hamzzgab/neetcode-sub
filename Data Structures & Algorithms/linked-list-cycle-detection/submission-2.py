# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head
        count = 0

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            if hare == turtle:
                return True
        return False