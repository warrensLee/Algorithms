from typing import List


# Function to perform heap sort
def heap_sort(arr: List[int]) -> None:
    # compute arr length once
    n = len(arr)

    # build the max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # heap sort
    for i in range(n - 1, 0, -1):
        # move max to end
        arr[0], arr[i] = arr[i], arr[0]  

        # restore & maintain heap  
        heapify(arr, i, 0)
    


# Helper function to maintain the max-heap property
def heapify(arr: List[int], n: int, i: int) -> None:
    # get the index and assume it is the largest,
    # its left child, and its right child
    largest, left, right = i, 2 * i + 1, 2 * i + 2

    # if left child is larger than index, update it
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child is larger than index, update it
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # if largest is not the parent, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

