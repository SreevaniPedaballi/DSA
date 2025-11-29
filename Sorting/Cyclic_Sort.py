"""
Cyclic Sort:
This algorithm works for arrays containing numbers in the range 1 to n (or 0 to n-1).
Each number should be placed at its correct index (value 1 → index 0, value 2 → index 1, etc.).
We check each index and if the current element is not in its correct position,
we swap it with the element at its correct index.
We move to the next index only when the current element is in the right position.
Time Complexity: O(n) — each number is swapped at most once.
Space Complexity: O(1) — in-place sorting.

"""

def Cyclic_Sort(arr):
    idx=0
    while idx <len(arr):
        correct_idx=arr[idx]-1
        if arr[idx] !=arr[correct_idx]:
            temp=arr[correct_idx]
            arr[correct_idx]=arr[idx]
            arr[idx]=temp
        else:
            idx +=1
            
    return arr
     
arr=[3,5,1,2,4]
print(Cyclic_Sort(arr))
