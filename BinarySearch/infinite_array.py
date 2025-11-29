
def infinite_arr_search(arr,target):
    if not arr:
        return -1
    s=0
    e=1
    while target> arr[e]:
        temp=e+1
        current_size=e-s+1
        new_size=current_size*2
        new_e=e+new_size 
        e=new_e if new_e < len(arr) else len(arr)-1
        s=temp
    
    return search(arr,target,s,e)


       
def search(arr,target,s_idx,e_idx):
    while s_idx <= e_idx:
        m= s_idx+(e_idx-s_idx)//2
        if target > arr[m]:
            s_idx=m+1
        elif target < arr[m]:
            e_idx=m-1
        else:
            return m
    return -1

arr=[1,2,3,4,5,6,7,8,10,13,15,18,20,24,26,29,30,32,33,35,36]
target=30
print(infinite_arr_search(arr,target))


