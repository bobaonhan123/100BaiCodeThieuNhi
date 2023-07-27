class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=""
        while len(num2)<len(num1):
            num2="0"+num2
        while len(num2)>len(num1):
            num1="0"+num1
        memo=0
        for i in range(len(num1)-1,-1,-1):
            p=int(num1[i])+int(num2[i])+memo
            res=str(p%10)+res
            memo=0 if p<10 else p//10
        if memo==0:
            return res
        return str(memo)+res
print(Solution().addStrings("456","77"))