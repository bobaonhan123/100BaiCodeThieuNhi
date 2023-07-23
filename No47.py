from typing import *
class Solution:
    def recursion(self, bits: List[int]) -> bool:
        if len(bits)==0:
            return True
        if len(bits)==1:
            if bits[0]==0:
                return True
            else:
                return False
        if bits[-1]==1 and bits[-2]==0:
            return False
        if len(bits)==2:
            return True
        condition1=False
        if(bits[-1]==0):
            condition1=self.recursion(bits[:-1])
        return condition1 or self.recursion(bits[:-2])
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return self.recursion(bits[:-1])
        
print(Solution().isOneBitCharacter([1,1,1,0]))