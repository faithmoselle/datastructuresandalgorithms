"""
AUTHOR: Faith Moselle O. Paule
DATE:

PROGRAM: Binary Tree Inorder Traversal
LANGUAGE: Python 3
TOPIC: DSA - Binary Tree Traversal (Inorder)
TECH STACK: Python Standard Library

INORDER TRAVERSAL ORDER:
1. Traverse left subtree
2. Visit root node
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


def InorderTraversal(root):
    """
    Recursively traverses tree in Inorder order.
    Algorithm: Left → Root → Right
    """
    if root:                              # Base case: node exists
        InorderTraversal(root.leftChild)  # Step 1: Visit left subtree
        print(root.data)                  # Step 2: Visit root
        InorderTraversal(root.rightChild) # Step 3: Visit right subtree


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

    print("\nInorder traversal of binary tree is")
    InorderTraversal(root)
    # Output: 5, 12, 6, 1, 9
