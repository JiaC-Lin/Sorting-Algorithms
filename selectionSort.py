# Similar to insertion-sort with comparisions but easier to understand. 
# Goes through the unsorted array finding the smallest element and swapping it with the first index in unsorted array. Therefore, we have sorted subarray at the beginning and the rest is unsorted.
# can be faster if we sort both the largest and smallest at the same time
from typing import List
from numpy import random

class Sort:
# swaps the 2 indexes (i, j) given
    def swap(self, arr:List[int], i: int, j:int):
        arr[i], arr[j] = arr[j], arr[i]

    def recurSelectionSort(self, arr: List[int]):
        pass

# Iterative Selection Sort:
#   O(n^2) time with O(1) space complexity
    def iterSelectionSort(self, arr: List[int]):
        N = len(arr)
        for i in range(N):
            # find the minimum element, starting with first element and making comparisons, in the unsorted sublist `A[i…n-1]` and swap it with `A[i]`
            min = i
            # Comparison array to find smallest element in unsorted subarray
            for j in range(i + 1, N):
                # if the `A[j]` element is less, then it is the new minimum
                if arr[j] < arr[min]:
                    min = j # update index of min element
            # swap minimum element in sublist `A[i…n-1]` with `A[i]`
            self.swap(arr, min, i)


A = random.randint(50, size=(7))
print(f"Unsorted Array is: {A}")
Sort().iterSelectionSort(A)
print(f"Sorted Array is: {A}")