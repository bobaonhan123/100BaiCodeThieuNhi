from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        tmp=0
        for i in nums:
            tmp=tmp+1 if i else 0
            res=max(res,tmp)
        return res
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))