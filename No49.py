from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        check1=[0 for i in range(len(nums))]
        check2=[0 for i in range(len(nums))]
        check1[0]=1
        check2[0]=1
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                check1[i]=1
            if nums[i]<=nums[i-1]:
                check2[i]=1
        return 0 not in check1 or 0 not in check2
    
print(Solution().isMonotonic([1,3,2]))