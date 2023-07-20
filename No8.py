class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res=""
        Set={'a', 'e', 'i', 'o', 'u'}
        newSet=set()
        for i in Set:
            newSet.add(i)
            newSet.add(chr(ord(i)-32))
        strArr=sentence.split(' ')
        for i in range(len(strArr)):
            if strArr[i][0] in newSet:
                strArr[i]+='ma'
            else:
                strArr[i]=strArr[i][1:]+strArr[i][0]+'ma'
            strArr[i]+=('a'*(i+1))
            res+=(' '+strArr[i])
        return res[1:]

print(Solution().toGoatLatin("The quick brown fox jumped over the lazy dog"))