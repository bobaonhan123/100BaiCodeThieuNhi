from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res^=i
        return res
print(Solution().singleNumber([-1]))
