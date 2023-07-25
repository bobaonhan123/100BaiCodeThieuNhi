from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp=dict()
        for i in nums:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1
        ma=0
        for i in mp:
            ma=max(ma,mp[i])
        c=[]
        c.extend(nums)
        c.reverse()
        mi=len(nums)
        for i in mp:
            if mp[i]==ma:
                mi=min(mi,len(c)-c.index(i)-nums.index(i))
        return mi
print(Solution().findShortestSubArray([1,2,2,3,1]))
