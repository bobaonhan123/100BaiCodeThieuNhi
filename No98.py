class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num<0:
            num = (1<<32)+num
        res=""
        while num>0:
            p=num%16
            if p<10:
                res=str(p)+res
            else:
                res=chr(p-10+ord('a'))+res
            num//=16
        return res
    
print(Solution().toHex(26))