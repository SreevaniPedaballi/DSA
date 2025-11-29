# https://leetcode.com/problems/first-missing-positive/
class FirstMissingPositive:
    def sort(self,arr):
        idx=0
        while idx < len(arr):
            correct_idx=arr[idx]-1
            if arr[idx]>0 and correct_idx<len(arr) and arr[idx]!=arr[correct_idx]:
                temp=arr[idx]
                arr[idx]=arr[correct_idx]
                arr[correct_idx]=temp
            else:
                idx += 1
        return arr
    

    def firstMissingPositive(self, nums: list[int]) -> int:
        arr=self.sort(nums)
        print(arr)
        for idx in range(len(arr)):
            if arr[idx] != idx+1:
                return idx+1
        return len(arr)+1
    
m=FirstMissingPositive()
nums=[3,4,-1,1]
print(m.firstMissingPositive(nums))