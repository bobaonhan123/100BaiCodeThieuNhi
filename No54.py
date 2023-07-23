from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        res=0
        for i in nums:
            res+=i-mi
        return res
print(Solution().minMoves([1,2,3]))
