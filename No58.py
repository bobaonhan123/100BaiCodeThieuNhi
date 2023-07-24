from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp=nums[0]
        cnt=0
        for i in nums:
            if cnt==0:
                tmp=i
            cnt+=1 if i==tmp else -1
        return tmp
print(Solution().majorityElement([2,2,1,1,1,2,2]))