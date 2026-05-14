"""
AUTHOR: Faith Moselle O. Paule
DATE:

PROGRAM: Menu-Driven Data Structures Demonstrator
LANGUAGE: Python 3
TOPIC: DSA - Lists, Linked Lists, Stacks, Queues, Trees
DESCRIPTION: Interactive menu to demonstrate 5 major data structures
"""

# ========== TREE FUNCTIONS ==========
class Menu:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(node):
    """Root → Left → Right"""
    if node:
        print(node.key, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    """Left → Root → Right"""
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)

def postorder(node):
    """Left → Right → Root"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=" ")

def leafcount(node):
    """Count nodes with no children"""
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return leafcount(node.left) + leafcount(node.right)


# ========== MAIN MENU ==========
while True:
    print("\n" + "=" * 40)
    print("Dashboard Menu")
    print("=" * 40)
    print("[1] - LIST (Linear Search)")
    print("[2] - LINKED LISTS (Circular)")
    print("[3] - STACKS (LIFO)")
    print("[4] - QUEUES (FIFO)")
    print("[5] - TREES (Binary Tree)")
    print("[6] - EXIT")
    print("=" * 40)

    try:
        option = int(input('Choose an operation (1-6): '))
    except ValueError:
        print("Invalid input. Please enter a number 1-6.")
        continue

    # ========== OPTION 1: LIST ==========
    if option == 1:
        print("\n--- LIST Selected (Linear Search) ---")
        size = int(input("Enter array size (1-10): "))
        if size < 1 or size > 10:
            print("Size must be between 1 and 10")
            continue
            
        items = []
        print("Enter array elements:")
        for i in range(size):
            items.append(int(input(f"Element {i+1}: ")))

        target = int(input("\nEnter element to search: "))

        found = False
        for i in range(size):
            if items[i] == target:
                print(f"{target} found at position {i+1}\n")
                found = True
                break
        if not found:
            print(f"{target} not found\n")

    # ========== OPTION 2: CIRCULAR LINKED LIST ==========
    elif option == 2:
        print("\n--- CIRCULAR LINKED LIST Selected ---")

        class Directory:
            class Node:
                def __init__(self, data):
                    self.data = data
                    self.next = None

            def __init__(self):
                self.head = None
                self.tail = None

            def add(self, data):
                new_node = self.Node(data)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                    new_node.next = self.head
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head

            def display(self):
                if self.head is None:
                    print("List is empty")
                    return
                current = self.head
                print("Nodes:", end=" ")
                while True:
                    print(current.data, end=" ")
                    current = current.next
                    if current == self.head:
                        break
                print()

            def total(self):
                if self.head is None:
                    return 0
                current = self.head
                total = 0
                while True:
                    total += current.data
                    current = current.next
                    if current == self.head:
                        break
                return total

        cd = Directory()
        print("Enter 5 numbers for circular linked list:")
        for i in range(5):
            data = int(input(f"Enter number {i+1}: "))
            cd.add(data)
        cd.display()
        print(f"Sum of all nodes: {cd.total()}\n")

    # ========== OPTION 3: STACK (CORRECTED) ==========
    elif option == 3:
        print("\n--- STACK Selected (LIFO) ---")
        
        class Stack:
            def __init__(self, size):
                self.arr = [0] * size
                self.capacity = size
                self.top = -1

            def push(self, x):
                if self.is_full():
                    print("Stack Overflow! Cannot push.")
                    return False
                self.top += 1
                self.arr[self.top] = x
                print(f"Pushed: {x}")
                return True

            def pop(self):
                if self.is_empty():
                    print("Stack Underflow! Cannot pop.")
                    return None
                popped = self.arr[self.top]
                self.top -= 1
                print(f"Popped: {popped}")
                return popped

            def is_empty(self):
                return self.top == -1

            def is_full(self):
                return self.top == self.capacity - 1

            def print_stack(self):
                if self.is_empty():
                    print("Stack is empty")
                    return
                print("Stack (top to bottom):", end=" ")
                for i in range(self.top, -1, -1):
                    print(self.arr[i], end=" ")
                print()

        stack = Stack(5)
        
        while True:
            print("\nStack Operations:")
            print("[1] Push")
            print("[2] Pop")
            print("[3] Print Stack")
            print("[4] Back to Main Menu")
            
            try:
                sub_option = int(input("Choice: "))
            except ValueError:
                print("Invalid input")
                continue
                
            if sub_option == 1:
                value = int(input("Enter value to push: "))
                stack.push(value)
            elif sub_option == 2:
                stack.pop()
            elif sub_option == 3:
                stack.print_stack()
            elif sub_option == 4:
                break
            else:
                print("Invalid choice")

    # ========== OPTION 4: QUEUE ==========
    elif option == 4:
        print("\n--- QUEUE Selected (FIFO) ---")
        print("Type 'done' to stop queueing")

        class Queue:
            def __init__(self):
                self.items = []

            def is_empty(self):
                return len(self.items) == 0

            def enqueue(self, item):
                self.items.append(item)
                print(f"Enqueued: {item}")

            def dequeue(self):
                if not self.is_empty():
                    removed = self.items.pop(0)
                    print(f"Dequeued: {removed}")
                    return removed
                else:
                    print("Queue is empty!")
                    return None

            def size(self):
                return len(self.items)
            
            def display(self):
                print("Queue:", self.items)

        queue = Queue()

        while True:
            user_input = input("Enter number (or 'done'): ")
            if user_input.lower() == 'done':
                break
            try:
                element = int(user_input)
                queue.enqueue(element)
            except ValueError:
                print("Invalid input. Please enter an integer.")

        print(f"\nYou have queued {queue.size()} elements")
        queue.display()

        while not queue.is_empty():
            queue.dequeue()

        print(f"Is Queue Empty? {queue.is_empty()}\n")

    # ========== OPTION 5: TREE ==========
    elif option == 5:
        print("\n--- BINARY TREE Selected ---")
        # Tree structure spelling "FAITH P."
        root = Menu("F")
        root.left = Menu("A")
        root.right = Menu("I")
        root.left.left = Menu("T")
        root.left.right = Menu("H")
        root.right.left = Menu("P")
        root.right.right = Menu(".")

        print("\nTree Traversals:")
        print("Preorder (Root→Left→Right): ", end="")
        preorder(root)
        print("\nInorder (Left→Root→Right): ", end="")
        inorder(root)
        print("\nPostorder (Left→Right→Root): ", end="")
        postorder(root)

        leaf_count = leafcount(root)
        print(f"\nNumber of leaf nodes: {leaf_count}\n")

    # ========== OPTION 6: EXIT ==========
    elif option == 6:
        print("\nThe program will now close. Goodbye!")
        break

    # ========== INVALID OPTION ==========
    else:
        print("Invalid choice. Option must be between 1 and 6. Try again.")
