from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp=[1 for i in range(len(nums))]
        ma=1
        for i in range(1,len(dp)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
                ma=max(ma,dp[i])
        return ma
print(Solution().findLengthOfLCIS([2,2,2,2,2]))