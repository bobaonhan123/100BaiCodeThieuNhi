from math import *
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bitnum=int(log2(n))
        key=1
        for i in range(bitnum):
            key<<=1
            if i%2!=0:
                key+=1
        return n^key==0

print(Solution().hasAlternatingBits(5))