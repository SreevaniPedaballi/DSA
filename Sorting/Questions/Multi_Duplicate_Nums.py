# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution1:
    def swap(self,arr,f_idx,s_idx):
        temp=arr[f_idx]
        arr[f_idx]=arr[s_idx]
        arr[s_idx]=temp
        return arr

    def sort(self,arr):
        idx=0
        while idx <len(arr):
            correct_idx=arr[idx]-1
            if arr[idx]!=arr[correct_idx]:
                arr=self.swap(arr,idx,correct_idx)
            else:
                idx += 1
        return arr

    def find_multi_duplicates(self, nums: list[int]) -> list[int]:
        arr=self.sort(nums)
        ans=[]
        for idx in range(len(arr)):
            if arr[idx]!=idx+1:
                ans.append(arr[idx])
        return ans

s = Solution1()
arr=[4,3,2,7,8,2,3,1]
print(arr)
ans=s.find_multi_duplicates(arr)
print(ans)