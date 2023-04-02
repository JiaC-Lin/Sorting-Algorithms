from typing import List
from numpy import random

class Sort:
    def swap(self, arr: List[int], i: int, j: int):
        arr[i], arr[j] = arr[j], arr[i]
    
    # Partitions by chooosing a pivot to seperate elements less and greater than the pivot. Lastly, place the pivot in their correct index
    # Returns index of the pivot in it's sorted position
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

# Recursion Quick Sort
    # Best and average time complexity: O(nlogn), worst case: O(n^2)
    # Best case space complexity: O(logn), worst case: O(n)
    # Recursively call quicksort where in each instance we partition the pivot using low and high arguments then doing the same quicksorting to both sides
    def recurQuickSort(self, arr: List[int], low: int, high: int):
        # Need base case to exit recursion
        if low < high: 
            # Sort the last element into their correct index
            part = self.partition(arr, low, high)
            # the part index contains the sorted element in it, need to sort the rest of the indexes around the sorted
            self.recurQuickSort(arr, low, part - 1)
            self.recurQuickSort(arr, part + 1, high)

# Iterative Quick Sort
    # Best and average time complexity: O(nlogn), worst case: O(n^2)
    # Space complexity: O(n)
    # Make a stack and push the low and high into stack to partition then we continue a while loop to pop out top two elements from stack into h and l. Using h and l, partition array for to sort the one element. Each time, we push 2 variables into stack if ((partition - 1) > l) or (partition + 1) < h) meaning we the array is not fully sorted. We pop out the next two elements in the stack to repeat the while loop again.
    def iterQuickSort(self, arr:List[int], low: int, high: int):
        # create auxilary stack
        stack = []
        # push/fill in stack
        stack.append(low)
        stack.append(high)

        while len(stack) >= 1:
            print(f"{stack}")
            # pop out high and low then into h and l
            h = stack.pop()
            l = stack.pop()
            # set pivot element in their correct position (part index) of sorted array
            part = self.partition(arr, l, h)
            # check if there are elements on left side or right side of part then push right side to stack
            if (part - 1) > l:
                stack.append(l)
                stack.append(part - 1)

            if (part + 1) < h:
                stack.append(part + 1)
                stack.append(h)

arr = [2, 3, 14, 31, 61, 9, 18, 19]
print(f"Unsorted Array is : {arr}")
N = len(arr)
Sort().recurQuickSort(arr, 0, N - 1)
print(f"Sorted Array is: {arr}", end="\n\n")

arr = random.randint(50, size=(10))
print(f"Unsorted Array: {arr}")
N = len(arr)
Sort().iterQuickSort(arr, 0 , N - 1)
print(f"Sorted Array is: {arr}", end="\n\n")