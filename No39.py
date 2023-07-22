class Solution:
    def addDigits(self, num: int) -> int:
        while(num>9):
            p=num
            t=0
            while(p>0):
                t+=p%10
                p//=10
            num=t
        return num

print(Solution().addDigits(38))