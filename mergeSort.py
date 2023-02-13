# divide the array into smaller pieces and sort them each time with each merge

from typing import List

class Sort:
# Recursively sort with O(nlogn) time and O(n) space complexity
    def mergeSort(self, arr:List[int]):
        size = len(arr)
        # base case: when array is of size 1, then it is already sorted
        if size > 1:
            mid = size // 2
            left = arr[:mid]
            right = arr[mid:]

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

            while i < sizeL:
                arr[k] = left[i]
                i += 1
                k += 1
            while j < sizeR:
                arr[k] = right[j]
                j += 1
                k += 1
# Iteratively sort
    def merge():
        pass
    def iterMergeSort():
        pass

arr = [12, 11, 13, 5, 6, 7]
Sort().mergeSort(arr)

print("Sorted Recursive Array is:")
size = len(arr)
for i in range(size):
    print(arr[i], end = " ")
print("\n")