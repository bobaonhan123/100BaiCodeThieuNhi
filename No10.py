from math import *
class Solution:
    def findComplement(self, num: int) -> int:return num^((1<<num.bit_length())-1)
print(Solution().findComplement(5))
    