"""
AUTHOR: Faith Paule
DATE: 

PROGRAM: Doubly Linked List Implementation
LANGUAGE: Python 3
TOPIC: Data Structures and Algorithms (DSA) - Doubly Linked Lists
TECH STACK: Python Standard Library

DESCRIPTION:
Implements a Doubly Linked List data structure where each node contains:
- Data value
- Pointer to previous node (prev)
- Pointer to next node (next)

ADVANTAGES over Singly Linked List:
- Can traverse in both directions (forward and backward)
- Deletion is more efficient (no need to find previous node)
- Insertion operations are simpler

OPERATIONS IMPLEMENTED:
1. insert_front() - Add node at beginning
2. insert_after() - Add node after a given node
3. insert_end() - Add node at the end
4. delete_node() - Remove a specific node
5. print_list() - Display all nodes forward

TIME COMPLEXITIES:
- Insert front: O(1)
- Insert after: O(1)
- Insert end: O(n) - requires traversal
- Delete node: O(1) - with reference to node
- Print list: O(n)
"""

class DoublyLinkedList:
    """
    Doubly Linked List class that manages a collection of nodes.
    Only tracks the head (first node), not the tail for simplicity.
    """
    
    # ========================================================================
    # INNER CLASS: Node
    # ========================================================================
    class Node:
        """
        Represents a single node in the doubly linked list.
        
        Attributes:
            data: The value stored in the node
            prev: Reference to the previous node (or None)
            next: Reference to the next node (or None)
        """
        
        def __init__(self, data):
            """
            Constructor - creates a new node with given data.
            
            Args:
                data: The value to store in the node
            """
            self.data = data      # Store the value
            self.prev = None      # Initially, no previous node
            self.next = None      # Initially, no next node

    # ========================================================================
    # LIST CONSTRUCTOR
    # ========================================================================
    def __init__(self):
        """
        Constructor - initializes an empty doubly linked list.
        Head points to None (no nodes in the list).
        """
        self.head = None          # First node in the list (or None if empty)

    # ========================================================================
    # INSERT AT FRONT
    # ========================================================================
    def insert_front(self, data):
        """
        Inserts a new node at the beginning of the list.
        
        Steps:
        1. Create new node
        2. Point new_node.next to current head
        3. Point new_node.prev to None (it's the new head)
        4. If list not empty, update old head's prev to new_node
        5. Update head to point to new_node
        
        Time Complexity: O(1) - constant time
        
        Args:
            data: The value to insert at the front
        """
        
        # Step 1: Create a new node
        new_node = self.Node(data)
        
        # Step 2: New node's next points to current head
        new_node.next = self.head
        
        # Step 3: New node's prev is None (it becomes the new head)
        new_node.prev = None
        
        # Step 4: If list not empty, update old head's prev
        if self.head is not None:
            self.head.prev = new_node
        
        # Step 5: Update head to new node
        self.head = new_node

    # ========================================================================
    # INSERT AFTER A SPECIFIC NODE
    # ========================================================================
    def insert_after(self, prev_node, data):
        """
        Inserts a new node after a given previous node.
        
        Steps:
        1. Validate prev_node is not None
        2. Create new node
        3. Set new_node.next to prev_node.next
        4. Set prev_node.next to new_node
        5. Set new_node.prev to prev_node
        6. If new_node has a next node, update its prev to new_node
        
        Time Complexity: O(1) - if we have reference to prev_node
        
        Args:
            prev_node: The node after which to insert (must be in list)
            data: The value to insert
        """
        
        # Validation: prev_node cannot be None
        if prev_node is None:
            print("previous node cannot be None")
            return
        
        # Step 1: Create new node
        new_node = self.Node(data)
        
        # Step 2: New node's next points to prev_node's next
        new_node.next = prev_node.next
        
        # Step 3: prev_node's next points to new node
        prev_node.next = new_node
        
        # Step 4: new node's prev points to prev_node
        new_node.prev = prev_node
        
        # Step 5: If new node is not the last node, update next node's prev
        if new_node.next is not None:
            new_node.next.prev = new_node

    # ========================================================================
    # INSERT AT END
    # ========================================================================
    def insert_end(self, data):
        """
        Inserts a new node at the end of the list.
        
        Steps:
        1. Create new node with next = None (will be last)
        2. If list empty, make it the head
        3. Otherwise, traverse to last node
        4. Link last node's next to new node
        5. Link new node's prev to last node
        
        Time Complexity: O(n) - must traverse to end of list
        Optimization: Could maintain tail pointer for O(1) append
        
        Args:
            data: The value to insert at the end
        """
        
        # Step 1: Create new node (next is None by default)
        new_node = self.Node(data)
        
        # Step 2: Start from head to traverse
        temp = self.head
        
        # Step 3: New node will be last, so next is None
        new_node.next = None
        
        # Step 4: Special case: empty list
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        # Step 5: Traverse to the last node
        while temp.next is not None:
            temp = temp.next
        
        # Step 6: Link last node to new node
        temp.next = new_node
        new_node.prev = temp

    # ========================================================================
    # DELETE A SPECIFIC NODE
    # ========================================================================
    def delete_node(self, del_node):
        """
        Deletes a specific node from the list.
        
        Steps:
        1. If list empty or node is None, do nothing
        2. If deleting head, update head to next node
        3. If node has next, update next node's prev to node's prev
        4. If node has prev, update prev node's next to node's next
        
        Time Complexity: O(1) - if we have reference to node to delete
        
        Args:
            del_node: The node to delete (must be in the list)
        """
        
        # Case 1: Empty list or invalid node
        if self.head is None or del_node is None:
            return
        
        # Case 2: Deleting the head node
        if self.head == del_node:
            self.head = del_node.next
        
        # Case 3: Update next node's prev pointer (if exists)
        if del_node.next is not None:
            del_node.next.prev = del_node.prev
        
        # Case 4: Update previous node's next pointer (if exists)
        if del_node.prev is not None:
            del_node.prev.next = del_node.next
        
        # Node is now orphaned - Python garbage collector will clean up

    # ========================================================================
    # PRINT LIST (FORWARD TRAVERSAL)
    # ========================================================================
    def print_list(self, node):
        """
        Prints all nodes in the list from given node to the end.
        Uses arrow (->) format to show links.
        
        Args:
            node: Starting node for printing (usually self.head)
        """
        
        # Start from the given node
        last = None
        
        # Traverse forward until end of list
        while node is not None:
            print(node.data, end="->")  # Print with arrow separator
            last = node                  # Keep track of last node
            node = node.next             # Move to next node
        
        print()  # New line after printing all nodes


# ============================================================================
# MAIN PROGRAM - TEST ALL OPERATIONS
# ============================================================================

if __name__ == "__main__":
    """
    Test driver for Doubly Linked List implementation.
    Demonstrates all operations: insert_front, insert_after, insert_end, delete_node.
    """
    
    # Create empty doubly linked list
    print("=" * 60)
    print("DOUBLY LINKED LIST DEMONSTRATION")
    print("=" * 60)
    
    doubly_ll = DoublyLinkedList()
    
    # ========== INSERTION OPERATIONS ==========
    print("\n1. Creating list with initial nodes...")
    doubly_ll.insert_end(5)        # List: 5
    doubly_ll.insert_front(1)      # List: 1 -> 5
    doubly_ll.insert_front(6)      # List: 6 -> 1 -> 5
    doubly_ll.insert_end(9)        # List: 6 -> 1 -> 5 -> 9
    
    print("   Current list: ", end="")
    doubly_ll.print_list(doubly_ll.head)
    
    # Insert 11 after head (after 6)
    print("\n2. Inserting 11 after head...")
    doubly_ll.insert_after(doubly_ll.head, 11)  # List: 6 -> 11 -> 1 -> 5 -> 9
    print("   After insert: ", end="")
    doubly_ll.print_list(doubly_ll.head)
    
    # Insert 15 after the second node (after 11)
    print("\n3. Inserting 15 after the second node...")
    doubly_ll.insert_after(doubly_ll.head.next, 15)  # List: 6 -> 11 -> 15 -> 1 -> 5 -> 9
    print("   After insert: ", end="")
    doubly_ll.print_list(doubly_ll.head)
    
    # Add 5 more nodes to the end
    print("\n4. Adding 5 more nodes to the end (22, 33, 44, 55, 66)...")
    doubly_ll.insert_end(22)
    doubly_ll.insert_end(33)
    doubly_ll.insert_end(44)
    doubly_ll.insert_end(55)
    doubly_ll.insert_end(66)
    print("   Final list: ", end="")
    doubly_ll.print_list(doubly_ll.head)
    
    # ========== DELETION OPERATION ==========
    # Delete the 6th node (counting from 1): 6(1), 11(2), 15(3), 1(4), 5(5), 9(6)
    print("\n5. Deleting the 6th node (value 9)...")
    doubly_ll.delete_node(doubly_ll.head.next.next.next.next.next)
    print("   After deletion: ", end="")
    doubly_ll.print_list(doubly_ll.head)
    
    print("\n" + "=" * 60)
    print("DOUBLY LINKED LIST OPERATIONS COMPLETE")
    print("=" * 60)
