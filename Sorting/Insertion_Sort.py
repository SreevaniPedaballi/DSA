"""
Insertion Sort is a simple comparison-based sorting algorithm.
It builds the sorted array one element at a time.

It starts from the second element and compares it with the elements before it.

It shifts elements that are larger than the current element to the right.

Then it inserts the current element into its correct position in the sorted portion of the array.

This process continues until the entire array is sorted.

It works similarly to how you insert cards into the correct position when sorting playing cards in your hands.

Time Complexity:
-------------------------------------------------------------
Best Case	Array is already sorted → only 1 comparison per element	O(n)
Average Case	Elements are in random order → shifting happens frequently	O(n²)
Worst Case	Array is sorted in reverse order → maximum shifts every time	O(n²)
"""

def insertion_sort(arr):
    for o_idx in range(len(arr)-1):#Here we need to consider only n-1 elements because the inner loop uses i+1. If we iterate up to n, the inner loop will go out of index
        for i_idx in range(o_idx+1,0,-1):
            if arr[i_idx] < arr[i_idx-1]:
                temp=arr[i_idx]
                arr[i_idx]=arr[i_idx-1]
                arr[i_idx-1]=temp
            else:
                break
    return arr

arr=[4,5,1,-3,0,2]
print(insertion_sort(arr))