"""
AUTHOR: Faith Paule
DATE:
Previous file name: LogarithmicTime

PROGRAM: Binary Search Algorithm
LANGUAGE: Python 3
TOPIC: DSA - Binary Search (Divide and Conquer)

TIME COMPLEXITY: O(log n) - logarithmic time
SPACE COMPLEXITY: O(1) - iterative implementation

REQUIREMENT: Array MUST be sorted
"""

def binary_search(arr, num):
    """
    Searches for target number in sorted array using binary search.
    
    Args:
        arr: Sorted list of integers
        num: Target number to find
    
    Returns:
        Index of target if found, -1 otherwise
    """
    low = 0                      # Start of search range
    high = len(arr) - 1          # End of search range
    
    while low <= high:
        mid = (low + high) // 2  # Middle index
        
        if arr[mid] < num:       # Target is in right half
            low = mid + 1
        elif arr[mid] > num:     # Target is in left half
            high = mid - 1
        else:                    # Target found
            return mid
    
    return -1                    # Target not found


# Test the binary search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 2

index = binary_search(arr, num)

if index != -1:
    print(f"{num} is at index {index}")
else:
    print(f"Element {num} could not be found.")
