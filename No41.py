from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        check=[False for i in range(len(nums)+1)]
        for i in nums:
            check[i]=True
        for i in range(1,len(check)):
            if not check[i]:
                res.append(i)
        return res
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))