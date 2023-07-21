class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        for i in range(left,right+1):
            tmp=i.bit_count()
            if tmp<2:
                continue
            else:
                for j in range(2,int(tmp**0.5)+1):
                    if tmp%j==0:
                        res-=1
                        break
                res+=1
        return res
    
print(Solution().countPrimeSetBits(6,10))