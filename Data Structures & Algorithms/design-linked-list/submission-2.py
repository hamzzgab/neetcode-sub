class Node:
    def __init__(self, prev=None, val=0, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class MyLinkedList:    

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head    

    def get(self, index: int) -> int:
        ptr = self.head.next
        while ptr is not self.tail and index > 0:
            index -= 1
            ptr = ptr.next
        
        if index > 0 or ptr is self.tail:
            return -1
        
        return ptr.val
        

    def addAtHead(self, val: int) -> None:
        prev, node, next = self.head, Node(val=val), self.head.next
        prev.next = node    
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtTail(self, val: int) -> None:
        prev, node, next = self.tail.prev, Node(val=val), self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        
    def addAtIndex(self, index: int, val: int) -> None:
        ptr = self.head.next
        while ptr is not self.tail and index > 0:            
            index -= 1
            ptr = ptr.next        

        if index > 0:
            return    
        
        prev, node, next = ptr.prev, Node(val=val), ptr
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        
    def deleteAtIndex(self, index: int) -> None:
        ptr = self.head.next
        while ptr is not self.tail and index > 0:
            index -= 1
            ptr = ptr.next

        if index > 0 or ptr is self.tail:
            return

        prev, next = ptr.prev, ptr.next
        prev.next = next
        next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)