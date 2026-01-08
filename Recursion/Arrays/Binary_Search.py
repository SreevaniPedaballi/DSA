def Binary_Search(arr,target,s_idx):
    arr_len=len(arr)
    if (s_idx >=arr_len):
        return -1
    is_target= s_idx if arr[s_idx]==target else -1
    if is_target !=-1:
        return is_target
    return Binary_Search(arr,target,s_idx+1)
arr=[1,2,13,21,32,12]
target=12
ans=Binary_Search(arr,target,0)
print(ans)


def Binary_Search(arr,target):
    if len(arr)==0:
        return False
    is_target_found= arr[0]==target
    if is_target_found:
        return True
    return Binary_Search(arr[1:],target)
ans=Binary_Search(arr,target)
print(ans)

def Binary_Search_Multiple_Occurences(arr,target,s_idx,res):
    if s_idx >=len(arr):
        return res
    is_found= s_idx if arr[s_idx] == target else -1
    if is_found!=-1:
        res.append(is_found)
    return Binary_Search_Multiple_Occurences(arr,target,s_idx+1,res)
    
arr=[12,1,2,12,13,12,21,32,12]
target=12
ans=Binary_Search_Multiple_Occurences(arr,target,0,[])
print(ans)

def Find_Index_Last(arr,target,idx):
    if idx<0:
        return False
    return arr[idx]==target or Find_Index_Last(arr,target,idx-1)
arr=[1,2,13,21,32,12]
target=12
ans=Find_Index_Last(arr,target,len(arr)-1)
print(ans)

def Find_Index_Last1(arr,target,idx):
    if idx<0:
        return -1
    is_found= idx if  arr[idx]==target else -1
    if is_found != -1:
        return is_found
    return Find_Index_Last1(arr,target,idx-1)
arr=[1,2,13,21,32,12]
target=12
ans=Find_Index_Last1(arr,target,len(arr)-1)
print(ans)


def Find_target_without_list_input(arr,target,s_idx):
    ans_list=[]
    if s_idx >=len(arr):
        return ans_list
    if arr[s_idx]==target:
        ans_list.append(s_idx)
    pre_ans_list=Find_target_without_list_input(arr,target,s_idx+1)
    ans_list.extend(pre_ans_list)
    return ans_list
    

arr=[1,12,3,12,14,12,15,12]
target=12
ans=Find_target_without_list_input(arr,target,0)
print(ans)


