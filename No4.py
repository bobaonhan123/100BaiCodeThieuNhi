from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        res=[]
        for i in candies:
            res.append(i+extraCandies>=maxCandies)
        return res
print(Solution().kidsWithCandies([2,3,5,1,3],3))