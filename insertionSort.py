# Sort array starting from leftmost. Starting from first element, sort one element at a time by shifting sorted subarray element(s) one by one to the right (while loop) until we find the correct index for new element. The new element, "key", is put into the correct spot by sorting the array on left side of key through comparison of bigger elements.

class Sort:
    # Worst Case: O(n^2), Average Case: O(n^2), Best Case: O(n)
    # Space Complexity of O(1)
    def insertionSort(self, arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i] # select first unsorted element

            j = i - 1
            # loop shifts elements to right to create position for element
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            # (j + 1) is j due to subtracting 1
            arr[j + 1] = key # inserts element into correct position

    # Space Complexity of O(n)
    def recurInsertionSort(self, arr, n):
        # n is length of array
        if n <= 1: # base case
            return
        
        # part 1: recursively sort first n-1 items which will go on till base case
        self.recurInsertionSort(arr, n - 1)

        # assuming n-1 items are in order
        # part 2: inserts the nth item into sorted part
        key = arr[n - 1]
        # n-1 is same as n since input n takes length of array starting at 1
        # same as the recursion technique, just recursively going up the array
        j = n - 2
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

                    

arr = [12, 11, 13, 5, 6]
Sort().insertionSort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\n")

arr = [12, 11, 13, 5, 6, 2]
n = len(arr)
Sort().recurInsertionSort(arr, n)
for i in range(len(arr)):
    print(arr[i], end=" ")