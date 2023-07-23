from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
        return list(set(res))
print(Solution().intersection([4,9,5], [9,4,9,8,4]))
