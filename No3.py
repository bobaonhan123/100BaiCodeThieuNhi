class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return format(x^y,'b').count('1')
    
print(Solution().hammingDistance(1,4))