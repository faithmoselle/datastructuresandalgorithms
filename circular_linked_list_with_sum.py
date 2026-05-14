"""
AUTHOR: Faith Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Circular Linked List with Sum Calculation
LANGUAGE: Python 3
TOPIC: Data Structures and Algorithms (DSA) - Circular Linked Lists
TECH STACK: Python Standard Library (Object-Oriented Programming)

DESCRIPTION:
Implements a Circular Linked List data structure where the last node points
back to the first node, forming a circle. This enhanced version includes:
1. Node creation and list management
2. Display all elements in circular order
3. Calculate sum of all integer values in the list

KEY FEATURES:
- Circular property: tail.next always points to head
- O(1) append operation (using tail pointer)
- O(n) traversal for display and sum calculation
- Memory-efficient singly linked nodes

USE CASES:
- Round-robin scheduling
- Game turn management
- Buffer implementations
- Operating system process queues

AUTHOR: [Student Name]
DATE: [Current Date]
"""

class CreateList:
    """
    Outer class representing the Circular Linked List.
    Manages head and tail pointers and provides list operations.
    """
    
    # ========================================================================
    # INNER CLASS: Node
    # ========================================================================
    class Node:
        """
        Represents a single node in the circular linked list.
        
        Attributes:
            data: The value stored in the node (expected to be numeric for sum)
            next: Reference/pointer to the next node in the list
        """
        
        def __init__(self, data):
            """
            Constructor for Node - creates a new node with given data.
            
            Args:
                data: The value to store in the node (typically integer)
            """
            self.data = data      # Store the data value
            self.next = None      # Initially, next points to nothing (None)

    # ========================================================================
    # MAIN LIST CONSTRUCTOR
    # ========================================================================
    def __init__(self):
        """
        Constructor for CreateList - initializes empty circular linked list.
        
        For an empty list:
        - head = None (no first node)
        - tail = None (no last node)
        """
        self.head = None    # Points to the first node in the list
        self.tail = None    # Points to the last node in the list

    # ========================================================================
    # ADD METHOD (Append to end)
    # ========================================================================
    def add(self, data):
        """
        Adds a new node to the end of the circular linked list.
        
        Maintains circular property: tail.next always points to head.
        
        Algorithm:
        1. Create new node with given data
        2. If list empty: new node becomes head and tail, points to itself
        3. If list not empty: add after tail, update tail, maintain circular link
        
        Time Complexity: O(1) - constant time operation
        
        Args:
            data: The value to add to the list
        """
        
        # Step 1: Create a new node with the provided data
        new_node = self.Node(data)

        # Step 2: Check if the list is empty
        if self.head is None:
            # Case 1: Empty list
            # Both head and tail point to the new node
            self.head = new_node
            self.tail = new_node
            # In a circular list with one node, it points to itself
            new_node.next = self.head  # Circular link to head
        else:
            # Case 2: List already has nodes
            # Current tail's next should point to new node
            self.tail.next = new_node
            # New node becomes the new tail
            self.tail = new_node
            # Maintain circular property: tail points back to head
            self.tail.next = self.head

    # ========================================================================
    # DISPLAY METHOD (Traverse and print all nodes)
    # ========================================================================
    def display(self):
        """
        Displays all nodes in the circular linked list.
        
        Since list is circular, we traverse until we return to head.
        Special handling for empty list.
        
        Algorithm:
        1. Start at head
        2. If list empty, print message
        3. Otherwise, traverse while printing each node's data
        4. Stop when we come back to head (completing the circle)
        
        Time Complexity: O(n) where n is number of nodes
        """
        
        # Start from the head node
        current = self.head
        
        # Case 1: List is empty
        if self.head is None:
            print("List is empty")
        
        # Case 2: List has nodes
        else:
            print("Nodes of the circular linked list:")
            
            # Traverse the circular list
            while True:
                # Print current node's data (without newline, space-separated)
                print(current.data, end=" ")
                
                # Move to the next node
                current = current.next
                
                # Stop condition: when we've returned to the head
                # This means we've completed one full circle
                if current == self.head:
                    break
            
            # Print new line after all nodes displayed
            print()

    # ========================================================================
    # SUM CALCULATION METHOD
    # ========================================================================
    def calculate_sum(self):
        """
        Calculates the sum of all data values in the circular linked list.
        
        Traverses the entire circle once, adding each node's data to a running total.
        
        Algorithm:
        1. Initialize total = 0
        2. If list not empty, traverse all nodes
        3. Add each node's data to total
        4. Stop when we return to head
        5. Return total (0 if list empty)
        
        Time Complexity: O(n) where n is number of nodes
        
        Returns:
            int/float: Sum of all data values in the list (0 if list empty)
        """
        
        # Start from the head node
        current = self.head
        total = 0
        
        # Only traverse if list is not empty
        if self.head is not None:
            # Traverse the circular list
            while True:
                # Add current node's data to running total
                total += current.data
                
                # Move to the next node
                current = current.next
                
                # Stop condition: when we've returned to the head
                if current == self.head:
                    break
        
        # Return the total (0 if list was empty)
        return total


# ============================================================================
# MAIN PROGRAM - USER INTERFACE
# ============================================================================

if __name__ == '__main__':
    """
    Main execution block - creates circular linked list, gets user input,
    displays all nodes, and calculates the sum of all values.
    
    NOTE: Original comment was misleading. This creates N nodes from scratch,
    not adding to an existing list of 3 nodes.
    """
    
    # Create an empty circular linked list
    cl = CreateList()
    
    # FIXED: Clear comment explaining actual behavior
    # Creates 9 nodes (i from 1 to 9 inclusive) based on user input
    print("Creating circular linked list with 9 nodes...")
    for i in range(1, 10):  # range(1,10) = [1,2,3,4,5,6,7,8,9] → 9 nodes
        data = int(input(f"Enter data for node {i}: "))
        cl.add(data)  # Add each node to the circular linked list

    # Display all nodes in the circular list
    cl.display()

    # Calculate and display the sum of all integer values
    sum_of_integers = cl.calculate_sum()
    print("Sum of Integers:", sum_of_integers)
