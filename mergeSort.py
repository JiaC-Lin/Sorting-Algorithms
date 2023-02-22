# divide the array into smaller and smaller pieces then sort them each time with each merge

from typing import List
import math

class Sort:
# Recursively sort with O(nlogn) time and O(n) space complexity
    def mergeSort(self, arr:List[int]):
        size = len(arr)
        # base case: when array is of size 1, then it is already sorted
        if size > 1:
            # split the array in half and create temporary new arrays to hold each half
            mid = size // 2
            left = arr[:mid]
            right = arr[mid:]

            # recursively call mergeSort on each half
            self.mergeSort(left)
            self.mergeSort(right)

            # set variables
            i, j, k = 0, 0, 0
            sizeL = len(left)
            sizeR = len(right)

            # Sort by comparing the smallest of two sets
            while i < sizeL and j < sizeR:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            # deal with the extra values after one set is finished
            while i < sizeL:
                arr[k] = left[i]
                i += 1
                k += 1
            while j < sizeR:
                arr[k] = right[j]
                j += 1
                k += 1

# Recursive sort 2 utilizing merge function with O(nlogn) time and O(n) space complexity
    def merge(self, left, right):
        # check if there is nothing to merge: length of one half is 0
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        
        arr = []
        totalSize = len(left) + len(right)
        i, j = 0, 0

        # Sort the 2 sides into one array
        while len(arr) < totalSize:
            if left[i] < right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1
            # if either half array is finished then append the rest of the other half to finish off arr
            if i == len(left) or j == len(right):
                arr.extend(left[i:] or right[j:])
        return arr
    
    def mergeSort2(self, arr:List[int]):
        # Base Case
        if len(arr) <= 1:
            return arr
        
        # split the array in half and create temporary new arrays to hold each half
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort each half
        rLeft = self.mergeSort2(left)
        rRight = self.mergeSort2(right)

        # Finally, mergesort the left and right half after each half is sorted
        return self.merge(rLeft, rRight)

# Iterative Sort with O(nlogn) time complexity and O(n) space complexity
    def iterMerge(self, a, l, m, r):
        # need to understand this -- holder for now
        n1 = m - l + 1
        n2 = r - m 
        L = [0] * n1 
        R = [0] * n2 
        for i in range(0, n1): 
            L[i] = a[l + i] 
        for i in range(0, n2): 
            R[i] = a[m + i + 1] 
    
        i, j, k = 0, 0, l 
        while i < n1 and j < n2: 
            if L[i] <= R[j]: 
                a[k] = L[i] 
                i += 1
            else: 
                a[k] = R[j] 
                j += 1
            k += 1
    
        while i < n1: 
            a[k] = L[i] 
            i += 1
            k += 1
    
        while j < n2: 
            a[k] = R[j] 
            j += 1
            k += 1

    def iterMergeSort(self, arr:List[int]):
        n = len(arr)
        for p in range(2, n + 1):
            for i in range(0, n + 1 - p):
                left = i
                right = i + p - 1
                mid = math.floor((left + right) / 2)

                self.iterMerge(arr, left, mid, right)

                i += p
            p *= 2
        if (p/2) < n :
            self.iterMerge(arr, 0, p/2, n-1)

arr = [12, 11, 13, 5, 6, 7]
Sort().mergeSort(arr)

print("Sorted Recursive Array is:")
size = len(arr)
for i in range(size):
    print(arr[i], end=" ")
print("\n")

arr = [11, 31, 7, 41, 101, 56, 76, 2]
output = Sort().mergeSort2(arr)

print("Sorted Recursive Array using merge function is:")
size = len(arr)
for i in range(size):
    print(output[i], end=" ")
print("\n")

arr = [2, 83, 23, 31, 51, 16, 8]
Sort().iterMergeSort(arr)

print("Sorted Iterative Array is:")
size = len(arr)
for i in range(size):
    print(arr[i], end=" ")
print("\n")