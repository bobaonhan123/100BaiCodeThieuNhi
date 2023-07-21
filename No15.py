from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard=[set([*"qwertyuiopQWERTYUIOP"]),set([*"asdfghjklASDFGHJKL"]),set([*"zxcvbnmZXCVBNM"])]
        res=[]
        for i in words:
            for j in keyboard:
                if set([*i]).issubset(j):
                    res.append(i)
        return res
    
print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))