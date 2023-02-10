# for both recursive and iterative heap sort: O(nlogn) time and O(1) for space complexity

from typing import List

class Sort:
    def swap(self, arr:List[int], i: int, j:int):
        arr[i], arr[j] = arr[j], arr[i]

# recursive heap sort
    # create a max heap where we order it into a descending binary tree
    # to heapify subtree rooted at index i
    # N is the upper limit or size of heap
    def heapify(self, arr: List[int], N: int, i: int):
        l = 2 * i + 1 # left child of parent node i
        r = 2 * i + 2 # right child
        parent = i

        # see if left child of root exists and is greater than root
        if l < N and arr[parent] < arr[l]:
            parent = l
        # see if right child of root exists and is greater than root
        if r < N and arr[parent] < arr[r]:
            parent = r

        # change root if needed
        if parent != i:
            self.swap(arr, i, parent)

            # heapify the new root/child of old parent -- go down tree
            self.heapify(arr, N, parent)

    def heapSort(self, arr: List[int]):
        N = len(arr) # starts at 1
        print(N)

        # build max heap with heapify
        for i in range(N//2 - 1, -1, -1): # stops and not include when at -1
            self.heapify(arr, N, i)

        # one by one extract elements
        for i in range(N - 1, 0, -1): # not include root -- no one to swap with
            self.swap(arr, i, 0)
            self.heapify(arr, i, 0) # reduced the range to i

# iterative heap sort
    def iterMinHeap(self, arr, n):
        for i in range(n):
            # if child bigger than parent
            if arr[i] > arr[int((i - 1) / 2)]:
                j = i
                # swap child and parent until parent is smaller
                while arr[j] > arr[int((j - 1) / 2)]:
                    self.swap(arr, j, int((j - 1) / 2))
                    j = int((j - 1) / 2)

    def iterHeapSort(self, arr, n):
        self.iterMinHeap(arr, n)

        for i in range(n - 1, 0, -1):
            # swap first index with last index
            self.swap(arr, 0, i)
            # maintain heap property after each swapping
            j = 0
            index = 0

            while True:
                index = 2 * j + 1
                
                # if left child is smaller than right child point index variable to right child
                if (index < (i - 1) and arr[index] < arr[index + 1]):
                    index += 1
                # if parent is smaller than child then swapping parent with child having higher value
                if index < i and arr[j] < arr[index]:
                    self.swap(arr, j, index)

                j = index 
                if index >= i:
                    break


arr = [12, 11, 13, 5, 6, 7, 2, 1]
Sort().heapSort(arr)

print("Sorted arry is:")
N = len(arr)
for i in range(N):
    print(arr[i], end=" ")
print("\n")

arr = [10, 20, 15, 17, 9, 21]
N = len(arr)
Sort().iterHeapSort(arr, N)

print("Sorted array is:")
for i in range(N):
    print(arr[i], end=" ")