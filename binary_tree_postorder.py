"""
AUTHOR: Faith Paule
DATE:

PROGRAM: Binary Tree Postorder Traversal
LANGUAGE: Python 3
TOPIC: DSA - Binary Tree Traversal (Postorder)
TECH STACK: Python Standard Library

POSTORDER TRAVERSAL ORDER:
1. Traverse left subtree
2. Traverse right subtree  
3. Visit root node

TIME COMPLEXITY: O(n) - visits each node once
SPACE COMPLEXITY: O(h) - recursion stack depth (h = tree height)
"""

class Node:
    """Represents a node in a binary tree."""
    
    def __init__(self, key):
        self.leftChild = None   # Left child reference
        self.rightChild = None  # Right child reference
        self.data = key         # Node value


def PostorderTraversal(root):
    """
    Recursively traverses tree in Postorder order.
    Algorithm: Left → Right → Root
    """
    if root:                               # Base case: node exists
        PostorderTraversal(root.leftChild)  # Step 1: Visit left subtree
        PostorderTraversal(root.rightChild) # Step 2: Visit right subtree
        print(root.data)                    # Step 3: Visit root


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

    print("\nPostorder traversal of binary tree is")
    PostorderTraversal(root)
    # Output: 5, 6, 12, 9, 1
