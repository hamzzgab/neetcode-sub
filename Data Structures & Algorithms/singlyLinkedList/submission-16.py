class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        counter = 0
        temp_ptr = self.head

        while temp_ptr:
            if counter == index:
                return temp_ptr.val

            temp_ptr = temp_ptr.next
            counter += 1

        return -1

    def insertHead(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp

    def insertTail(self, val):
        if self.head is None:
            self.insertHead(val)
        else:
            temp_ptr = self.head
            while temp_ptr.next is not None:
                temp_ptr = temp_ptr.next
            temp_ptr.next = Node(val)

    def remove(self, index):
        temp_ptr = self.head
        length = 0

        while temp_ptr:
            temp_ptr = temp_ptr.next
            length += 1

        if (self.head is None) or (index >= length):
            return False
        elif index == 0:
            self.head = self.head.next
            return True
        else:
            counter = 0
            temp_ptr = self.head

            while counter < (index - 1):
                temp_ptr = temp_ptr.next
                counter += 1

            temp_ptr.next = temp_ptr.next.next
            return True

    def getValues(self):
        temp_ptr = self.head
        arr = []
        while temp_ptr:
            arr.append(temp_ptr.val)
            temp_ptr = temp_ptr.next

        return arr