"""
AUTHOR: Faith Moselle O. Paule
DATE:

PROGRAM: Binary Tree Preorder Traversal
FILE: binary_tree_preorder.py
LANGUAGE: Python 3
TOPIC: DSA - Binary Tree Traversal (Preorder)
TECH STACK: Python Standard Library

PREORDER TRAVERSAL ORDER:
1. Visit root node
2. Traverse left subtree
3. Traverse right subtree

TIME COMPLEXITY: O(n) - visits each node once
SPACE COMPLEXITY: O(h) - recursion stack depth (h = tree height)
"""

class Node:
    """Represents a node in a binary tree."""
    
    def __init__(self, key):
        self.leftChild = None   # Left child reference
        self.rightChild = None  # Right child reference
        self.data = key         # Node value


def PreorderTraversal(root):
    """
    Recursively traverses tree in Preorder order.
    Algorithm: Root → Left → Right
    """
    if root:                               # Base case: node exists
        print(root.data)                    # Step 1: Visit root
        PreorderTraversal(root.leftChild)  # Step 2: Visit left subtree
        PreorderTraversal(root.rightChild) # Step 3: Visit right subtree


if __name__ == "__main__":
    # Create binary tree structure:
    #        1
    #      /   \
    #    12     9
    #   /  \
    #  5    6
    
    root = Node(1)
    root.leftChild = Node(12)
    root.rightChild = Node(9)
    root.leftChild.leftChild = Node(5)
    root.leftChild.rightChild = Node(6)

    print("\nPreorder traversal of binary tree is")
    PreorderTraversal(root)
    # Output: 1, 12, 5, 6, 9
