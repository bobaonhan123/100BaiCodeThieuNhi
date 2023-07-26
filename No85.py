from math import *
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return str(0)
        res=""
        resStr=""
        if num<0:
            resStr='-'
            num=abs(num)
        while num!=0:
            res = str(num%7)+res
            num//=7
        return resStr+res
print(Solution().convertToBase7(100))