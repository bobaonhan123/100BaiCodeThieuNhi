class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr=[*magazine]
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in arr:
                arr.remove(ransomNote[i])
                continue
            else:
                return False
        return True 
print(Solution().canConstruct("aa","aba"))