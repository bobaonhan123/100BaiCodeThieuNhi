from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        res=max(nums)
        i=nums.index(res)
        nums.remove(res)
        return i if res>=max(nums)*2 else -1
print(Solution().dominantIndex([3,6,1,0]))