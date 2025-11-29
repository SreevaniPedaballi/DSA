# https://leetcode.com/problems/set-mismatch/
class Solution3:
    def swap(arr,f_idx,s_idx):
        temp=arr[f_idx]
        arr[f_idx]=arr[s_idx]
        arr[s_idx]=temp
        return arr
    
    def sort(self,arr):
        idx=0
        while idx <len(arr):
            correct_idx=arr[idx]-1
            if arr[idx]!=arr[correct_idx]:
                self.swap(arr,idx,correct_idx)
            else:
                idx +=1
        return arr


    def findErrorNums(self, nums: list[int]) -> list[int]:
        arr=self.sort(nums)
        ans=[]
        for idx in range(len(arr)):
            if arr[idx]!=idx+1:
                ans.extend([arr[idx],idx+1])
                return ans
        return ans

s = Solution3()
arr=[1,1]
print(arr)
ans=s.findErrorNums(arr)
print(ans)