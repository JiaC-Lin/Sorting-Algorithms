# worst case: O(n^2)
# best and average time complexity: O(nlogn) and worst case space O(n) and best case O(logn)

from typing import List
from numpy import random

class Sort:
    def swap(self, arr: List[int], i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(self, arr: List[int], low: int, high: int):
        # uses last element as a PIVOT which can be optimized to be random
        pivot = arr[high]
        # indexing for the next swap of number lower than pivot with current element
        i = low 
        # Go through partition of array and seperate (the elements lower than pivot)from (elements greater than pivot)
        for j in range(low, high):
            if arr[j] <= pivot:
                self.swap(arr, i, j)
                i += 1
        # after traversal, swap pivot element with index keeping elements lower than pivot to the left and elements greater than pivot to the right
        self.swap(arr, i, high)

        # return pivot in their 'correct' index
        return i

    def recurQuickSort(self, arr: List[int], low: int, high: int):
        # Need base case to exit recursion
        if low < high: 
            # Sort the last element into their correct index
            part = self.partition(arr, low, high)
            # the part index contains the sorted element in it, need to sort the rest of the indexes around the sorted
            self.recurQuickSort(arr, low, part - 1)
            self.recurQuickSort(arr, part + 1, high)

    def iterQuickSort(self, arr:List[int], low: int, high: int):
        # create auxilary stack
        stack = [0] * (high - low + 1)
        top = 0
        stack[top] = low
        top += 1
        stack[top] = high
        while top >= 0:
            pass

arr = [2, 3, 14, 31, 61, 9, 18, 19]
print(f"Unsorted Array is : {arr}")
N = len(arr)
Sort().recurQuickSort(arr, 0, N - 1)
print(f"Sorted Array is: {arr}", end="\n\n")

arr = random.randint(50, size=(7))
print(f"Unsorted Array: {arr}")
N = len(arr)
Sort().iterQuickSort(arr, 0 , N - 1)
print(f"Sorted Array is: {arr}", end="\n\n")