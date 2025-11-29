"""
Bubble sort is also known as sinking sort or exchange sort.
Its best-case time complexity is O(N) when the array is already sorted in ascending order.
The worst-case time complexity is O(N²) when the array is sorted in descending order.
In each pass, the maximum element moves to the last index, so we skip comparing the last index in the next iteration (end–1).
If the array is already sorted in ascending order, we break out of the loop.
"""
def bubble_sort(arr):
    end=len(arr)-1
   
    while end >=0 and end <len(arr):
        is_swapped=False
        for idx in range(end+1):
            if idx+1<len(arr) and arr[idx] > arr[idx+1]:
                temp=arr[idx]
                arr[idx]=arr[idx+1]
                arr[idx+1]=temp
                is_swapped=True
        if not is_swapped:
            break
        end -=1
    return arr
arr=[1,-3,0,4,2]
print(bubble_sort(arr))





