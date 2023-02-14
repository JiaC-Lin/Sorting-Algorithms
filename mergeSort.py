# divide the array into smaller and smaller pieces then sort them each time with each merge

from typing import List

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

            i, j, k = 0, 0, 0
            sizeL = len(left)
            sizeR = len(right)

            while i < sizeL and j < sizeR:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            # deal with the extra values after one side is finished
            while i < sizeL:
                arr[k] = left[i]
                i += 1
                k += 1
            while j < sizeR:
                arr[k] = right[j]
                j += 1
                k += 1

# Recursive sort 2 utilizing merge function
    def merge(self, left, right):
        # check if there is nothing to merge: length of one half is 0
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        
        arr = []
        totalSize = len(left) + len(right)
        i, j = 0, 0

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
        if len(arr) <= 1:
            return arr
        
        # split the array in half and create temporary new arrays to hold each half
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        rLeft = self.mergeSort2(left)
        rRight = self.mergeSort2(right)

        return self.merge(rLeft, rRight)

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

