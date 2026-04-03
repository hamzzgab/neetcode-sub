class Tree:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        new_node = Tree(key, val)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMax(self):
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def getMin(self):
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getInorderKeys(self):
        result = []
        self.inorder(self.root, result)
        return result

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.key)
            self.inorder(node.right, result)

    def remove(self, key):
        self.root = self.remove_helper(self.root, key)

    @staticmethod
    def find_minion(node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def remove_helper(self, node, key):
        if node is None:
            return None
        
        if key > node.key:
            node.right = self.remove_helper(node.right, key)
        elif key < node.key:
            node.left = self.remove_helper(node.left, key)            
        else:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            max_node = self.find_minion(node.right)
            node.val = max_node.val
            node.key = max_node.key
            node.right = self.remove_helper(node.right, node.key)
        return node