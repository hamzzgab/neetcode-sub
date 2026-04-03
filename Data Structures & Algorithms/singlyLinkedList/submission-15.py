from itertools import count
from typing import List


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.node = None

    def get(self, index: int) -> int:
        search = 0
        ptr = self.node
        while search <= index and ptr:
            if search == index:
                return ptr.data
            search += 1
            ptr = ptr.next
        return -1

    def insertHead(self, val: int) -> None:
        head = ListNode(val)
        head.next = self.node
        self.node = head

    def insertTail(self, val: int) -> None:
        if self.node is None:
            self.insertHead(val)
        else:
            new_node = ListNode(val)
            ptr = self.node
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node

    def remove(self, index: int) -> bool:
        ptr = self.node
        pre = None
        if index == 0:
            if ptr:
                self.node = ptr.next
                return True
            else:
                return False

        for i in range(index):
            pre = ptr
            ptr = ptr.next
            if not ptr:
                return False
        pre.next = ptr.next
        return True

    def getValues(self) -> List[int]:
        ptr = self.node
        res = []
        if ptr:
            while ptr:
                res.append(ptr.data)
                ptr = ptr.next
            return res
        else:
            return res
