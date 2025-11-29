"""
In selection sort, we find the maximum element in the array and place it in its correct position (at the end).
After each step, the maximum element is already at the last position, so we can ignore the last elements in each subsequent iteration.
The time complexity in both the best and worst cases is O(n²).
"""

def find_max_index(arr):
    max_idx=0
    for idx in range(len(arr)):
        if arr[max_idx] < arr[idx]:
            max_idx=idx
    return max_idx

def swap(arr,first_idx,second_idx):
    temp=arr[first_idx]
    arr[first_idx]=arr[second_idx]
    arr[second_idx]=temp

    return arr

def selection_sort(arr):
    end_idx=len(arr)-1
    while end_idx >=0 and end_idx <len(arr):
        max_idx=find_max_index(arr[:end_idx+1])
        arr=swap(arr,max_idx,end_idx)
        end_idx -=1
    return arr

arr=[4,5,1,3,2]
print(selection_sort(arr))
