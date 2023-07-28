from typing import List
class Solution:
    def recursion(self,n:int,check:List[bool])->bool:
        if n==1:
            return True
        if n in check:
            return False
        check.add(n)
        res=0
        while n>0:
            res+=(n%10)**2
            n//=10
        
        return self.recursion(res,check) 
    def isHappy(self, n: int) -> bool:
        return self.recursion(n,set())
print(Solution().isHappy(19))