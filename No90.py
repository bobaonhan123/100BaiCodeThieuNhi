from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        l=prices[0]
        for i in prices[1:]:
            if i>l:
                res=max(res,i-l)
            else:
                l=i
        return res

print(Solution().maxProfit([7,1,5,3,6,4]))