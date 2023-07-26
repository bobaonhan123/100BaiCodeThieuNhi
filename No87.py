class Solution:
    def reverse_sublist(self, lst, start, end):
        for i in range(start,start+(end-start+1)//2):
            lst[i],lst[end-(i-start)]=lst[end-(i-start)],lst[i]
        return lst
    
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        res=""
        n=len(s)
        li=[*s]
        while i<n:
            if i+k<= n:
                li=self.reverse_sublist(li,i,i+k-1)
            else:
                li=self.reverse_sublist(li,i,n-1)
            i+=2*k
        for j in li:
            res+=j
        return res
print(Solution().reverseStr("abcdefg", 2))