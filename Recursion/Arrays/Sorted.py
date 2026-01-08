def sorted1(arr:int,s_idx)->bool:
    arr_len=len(arr)
    if s_idx >=arr_len or s_idx+1>=arr_len  :
        return True
    is_sorted=True if arr[s_idx]<arr[s_idx+1] else False
    if not is_sorted:
        return False
    return is_sorted and sorted1(arr,s_idx+1)

def sorted2(arr):
    if not arr or len(arr)<=1:
        return True
    is_sorted=arr[0]<arr[1]
    if not is_sorted:
        return False
    return is_sorted and sorted2(arr[1:])
    
arr=[1,0]
ans1=sorted1(arr,0)
print(ans1)

ans2=sorted2(arr)
print(ans2)
  


