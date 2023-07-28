from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp=dict()
        for i in nums:
            if i not in mp:
                mp[i]=0
            mp[i]+=1
        ma=0
        for i in mp:
            if i+1 in mp:
                ma=max(ma,mp[i]+mp[i+1])
        return ma
print(Solution().findLHS([1,3,2,2,5,2,3,7]))
