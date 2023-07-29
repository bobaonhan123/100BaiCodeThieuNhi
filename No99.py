class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        a,b,c=1,1,0
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return c
print(Solution().climbStairs(3))