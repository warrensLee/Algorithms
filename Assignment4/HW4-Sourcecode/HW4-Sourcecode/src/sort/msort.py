from typing import List, TypeVar

T = TypeVar("T")

def merge(array: List[T], l: int, m: int, r: int) -> None:
    # get the left and right side
    left = array[l:m + 1]
    right = array[m + 1:r + 1]

    # pointers for left, right, & merged array
    i, j, k = 0, 0, l

    # merge until one side runs out
    while i < len(left) and j < len(right):
        # compare elements from both halves
        if left[i] <= right[j]:
            # set the smaller element to the
            # correct position in given array
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    # if left and right are not the same size,
    # one will finish first, so this will handle
    # the rest of left's elements.  
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def msort(array: List[T], l: int, r: int) -> None:
    if l < r:
        m = (l + r) // 2                # get middle index
        msort(array, l, m)              
        msort(array, m + 1, r)          # recursively sort left & right side
        merge(array, l, m, r)           # combine those halves into one section

