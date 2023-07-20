from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            bl=True
            p=i
            while p>0:
                if (p%10)==0 or not i%(p%10)==0:
                    bl=False
                    break
                p//=10
            if bl:
                res.append(i)
        return res
print(Solution().selfDividingNumbers(47,85))