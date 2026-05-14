"""
AUTHOR: Faith Moselle O. Paule
DATE: 

PROGRAM: Binary Tree Leaf Node Counter
LANGUAGE: Python 3
TOPIC: Data Structures and Algorithms (DSA) - Binary Trees
TECH STACK: Python Standard Library

DESCRIPTION:
Implements a binary tree data structure and counts the number of leaf nodes.
A leaf node is a node that has no children (both left and right are None).

TREE STRUCTURE:
        p
       / \
      g   w
     / \  / \
    c  k s  y
   / \ /\/ / \
  a e i m q u x z

LEAF NODES: a, e, i, m, q, u, x, z → Total: 8

ALGORITHM:
- If node is None: return 0 (empty tree/subtree)
- If node has no children: return 1 (this is a leaf)
- Otherwise: recursively count leaves in left + right subtrees

TIME COMPLEXITY: O(n) where n = number of nodes
SPACE COMPLEXITY: O(h) where h = height of tree (recursion stack)
"""

# ============================================================================
# NODE CLASS - Represents each node in the binary tree
# ============================================================================

class Node:
    """
    Represents a single node in a binary tree.
    
    Attributes:
        data: The value stored in the node (can be any type)
        left: Reference to the left child node (or None)
        right: Reference to the right child node (or None)
    """
    
    def __init__(self, data):
        """
        Constructor - creates a new node with given data.
        
        Args:
            data: The value to store in the node (character in this example)
        """
        self.data = data      # Store the node's value
        self.left = None      # Initially, no left child
        self.right = None     # Initially, no right child


# ============================================================================
# LEAF COUNT FUNCTION - Recursively counts leaf nodes
# ============================================================================

def leafCount(node):
    """
    Recursively counts the number of leaf nodes in a binary tree.
    
    A leaf node is defined as a node with both left and right children as None.
    
    Algorithm:
    1. Base Case 1: If node is None (empty tree) → return 0
    2. Base Case 2: If node has no children (leaf) → return 1
    3. Recursive Case: return leafCount(left) + leafCount(right)
    
    Parameters:
        node (Node): The root node of the tree/subtree to examine
        
    Returns:
        int: The total number of leaf nodes in the tree/subtree
        
    Time Complexity: O(n) - visits each node exactly once
    Space Complexity: O(h) - recursion stack depth = tree height
    """
    
    # Base Case 1: Empty node (reached beyond leaf)
    # Example: node.left when node is a leaf → None
    if node is None:
        return 0
    
    # Base Case 2: Leaf node found (no children)
    # Example: node with both left and right = None
    if node.left is None and node.right is None:
        return 1  # This node itself is a leaf
    
    # Recursive Case: Node has at least one child
    # Count leaves in left subtree + leaves in right subtree
    else:
        return leafCount(node.left) + leafCount(node.right)


# ============================================================================
# MAIN PROGRAM - Construct tree and count leaves
# ============================================================================

if __name__ == '__main__':
    """
    Main execution block - builds a binary tree and counts leaf nodes.
    Tree is constructed to spell out words/letters in a specific pattern.
    """
    
    # Create root node with value 'p'
    # The tree spells out words when read in-order or creates a pattern
    root = Node('p')
    
    # ========== LEFT SUBTREE ==========
    # Build the left side of the tree
    root.left = Node('g')                    # Level 2 left
    root.left.left = Node('c')               # Level 3 left-left
    root.left.left.left = Node('a')          # Level 4 leaf
    root.left.left.right = Node('e')         # Level 4 leaf
    root.left.right = Node('k')              # Level 3 left-right
    root.left.right.left = Node('i')         # Level 4 leaf
    root.left.right.right = Node('m')        # Level 4 leaf
    
    # ========== RIGHT SUBTREE ==========
    # Build the right side of the tree
    root.right = Node('w')                   # Level 2 right
    root.right.left = Node('s')              # Level 3 right-left
    root.right.left.left = Node('q')         # Level 4 leaf
    root.right.left.right = Node('u')        # Level 4 leaf
    root.right.right = Node('y')             # Level 3 right-right
    root.right.right.left = Node('x')        # Level 4 leaf
    root.right.right.right = Node('z')       # Level 4 leaf
    
    # ========== COUNT AND DISPLAY LEAF NODES ==========
    # Calculate total number of leaf nodes using recursive function
    # Output format uses %d for integer (old-style formatting)
    print("Total Leaf Nodes = %d" % (leafCount(root)))
