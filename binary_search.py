# Write a Python class that represents a binary search tree, with methods for inserting a value into the tree, deleting a value from the tree, and checking if a value is in the tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        def _delete(node, value):
            if node is None:
                return node
            elif value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if node.left is None and node.right is None:
                    node = None
                elif node.left is None:
                    node = node.right
                elif node.right is None:
                    node = node.left
                else:
                    temp = self._find_min(node.right)
                    node.value = temp.value
                    node.right = _delete(node.right, temp.value)
            return node

        self.root = _delete(self.root, value)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current