from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if not i%2:
                res.append(i)
        for i in nums:
            if i%2:
                res.append(i)
        return res
print(Solution().sortArrayByParity([3,1,2,4]))