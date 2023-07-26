from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            res^=i
            res^=nums[i]
        res^=len(nums)
        return res
    
print(Solution().missingNumber([0,1,3,2,5]))