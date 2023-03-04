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
    def recurMerge(self, left:List[int], right:List[int]):
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
        return self.recurMerge(rLeft, rRight)

# Bottom-Up (smaller to bigger) Iterative Sort with O(nlogn) time complexity and O(n) space complexity
# Start sorting all subarrays of length 1, by definition is already sorted. Then sort all subarrays of length 2 by merging length-1 subarrays. Then sort all subarrays of length 4 by merging length-2 subarrays. Repeat till whole array is sorted.
# [       chunk 1       ]       [       chunk 2     ]
# [ l | m ]     [---| r ]       [ l | m ]       [ r ]           //sub_size of 2
# [ l |---|---| m ]     [---|---| r ]                           //sub_size of 4
# [---|---|---|---|---|---|---]                                 //sub_size of 8
    def iterMerge(self, arr:List[int], l:int, m:int, r:int):
        # determine the size of left and right arrays
        n1 = m - l + 1 
        n2 = r - m 
        # allocate an array with space of n1 and n2
        Left = [0] * n1 
        Right = [0] * n2 
        # fill in the left and right array with the 2 arrays we want to mergesort
        for i in range(0, n1): 
            Left[i] = arr[l + i] 
        for i in range(0, n2): 
            Right[i] = arr[m + i + 1] 
    
        # mergesorting 2 arrays back into the original starting at position 'l', similar to recursive merge while in place
        # Sort by comparing the smallest of two sets
        i, j = 0, 0 
        while i < n1 and j < n2: 
            if Left[i] <= Right[j]: 
                arr[l] = Left[i] 
                i += 1
            else: 
                arr[l] = Right[j] 
                j += 1
            l += 1
    
        # deal with the extra values after one set is finished
        while i < n1: 
            arr[l] = Left[i] 
            i += 1
            l += 1
        while j < n2: 
            arr[l] = Right[j] 
            j += 1
            l += 1
 
    def iterMergeSort(self, arr:List[int]):
        n = len(arr)
        # sub_size start with least partition size of 2^0 = 1 then multiply sub_size by 2 (until sub_size reaches n or higher) since subarray size grows by powers of 2. Start at 2 because with partition size 1 means its already merged with itself and sorted to itself
        for sub_size in range(2, n):
            # always start from leftmost and no need to sort the last element as it won't be merging with anything
            for i in range(0, n - 1):
                left = i
                # using left as indicator of the next batch we find the mid and right while keeping in mind not to take a value OUT OF RANGE therefore we take minimum with the last index
                mid = min(left + sub_size - 1, n - 1)
                right = min(left + 2 * sub_size - 1, n - 1)
                # final merge should consider unmerged sublist if input arr size is not power of 2
                self.iterMerge(arr, left, mid, right)
                
                # go to the next chunk (see image diagram) to merge the next 2 arrays
                i += (sub_size * 2)
            # increase sub array size by multiplication power of 2 after each merge
            sub_size *= 2 

arr = [12, 11, 13, 5, 6, 7, 1]
Sort().mergeSort(arr)

print("Sorted Recursive Array is:")
size = len(arr)
for i in range(size):
    print(arr[i], end=" ")
print("\n")

arr = [11, 31, 7, 41, 101, 56, 76, 2, 99]
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