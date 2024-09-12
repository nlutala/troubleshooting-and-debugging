"""
troubleshoot_8.py

Troubleshoot the issue 8: (created by Generative AI)

Author: Nathan Lutala (nlutala)

Nothing to debug here, the code is correct
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)


if __name__ == "__main__":
    root = Node(10)
    keys = [20, 5, 6, 15, 30, 25, 35]
    for key in keys:
        insert(root, key)

    inorder_traversal(root)
