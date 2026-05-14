"""
AUTHOR: Faith Moselle O. Paule
DATE: 

PROGRAM: Stack Implementation (Array-based)
LANGUAGE: Python 3
TOPIC: Data Structures - Stack (LIFO - Last In, First Out)
TECH STACK: Python Standard Library

OPERATIONS:
- push(): Add element to top (O(1))
- pop(): Remove element from top (O(1))
- is_empty(): Check if stack has no elements
- is_full(): Check if stack has reached capacity
- get_size(): Return number of elements
- print_stack(): Display all elements
"""

class Stack:
    """Stack implementation using a fixed-size array."""
    
    def __init__(self, size):
        """Initialize empty stack with given capacity."""
        self.arr = [0] * size    # Fixed-size array
        self.top = -1             # Empty stack indicator
        self.capacity = size      # Maximum size

    def push(self, x):
        """Add element to top of stack."""
        if self.is_full():
            print("Stack Overflow")  # Stack is full
            return
        self.top += 1
        self.arr[self.top] = x
        print("Inserting", x)

    def pop(self):
        """Remove and return top element."""
        if self.is_empty():
            print("Stack Empty")  # Stack has no elements
            return
        item = self.arr[self.top]
        self.top -= 1
        return item

    def get_size(self):
        """Return current number of elements."""
        return self.top + 1

    def is_empty(self):
        """Check if stack has no elements."""
        return self.top == -1

    def is_full(self):
        """Check if stack has reached capacity."""
        return self.top == self.capacity - 1

    def print_stack(self):
        """Display all elements from bottom to top."""
        for i in range(self.top + 1):
            print(self.arr[i], end=", ")
        print()


if __name__ == '__main__':
    # Get stack size from user
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)

    # Interactive menu
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Print Stack")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to push: "))
            stack.push(data)
        elif choice == '2':
            if stack.is_empty():
                print("Stack is empty. Cannot pop.")
            else:
                popped = stack.pop()
                print("Popped element:", popped)
        elif choice == '3':
            print("Stack: ", end="")
            stack.print_stack()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
