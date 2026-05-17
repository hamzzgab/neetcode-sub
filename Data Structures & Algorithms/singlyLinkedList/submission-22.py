class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = Node(val=-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i, ptr = 0, self.head.next
        while i < index and ptr:
            i += 1
            ptr = ptr.next
        
        if ptr:
            return ptr.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next    

    def remove(self, index: int) -> bool:
        i, ptr = 0, self.head
        while i < index and ptr:
            i += 1
            ptr = ptr.next
        if ptr and ptr.next:
            if self.tail == ptr.next:
                self.tail = ptr
            ptr.next = ptr.next.next
            return True
        return False
        
    def getValues(self) -> List[int]:
        ptr, res = self.head.next, []
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next        
        return res
        
