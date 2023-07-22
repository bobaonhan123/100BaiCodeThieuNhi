class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        if ord(word[0])>ord('Z'):
            for i in range(len(word)):
                if ord(word[i])>=ord('A') and ord(word[i])<=ord('Z'):
                    return False
        if ord(word[0])<=ord('Z'):
            if len(word)==2:
                return True
            if ord(word[1])>ord('Z'):
                for i in range(2,len(word)):
                    if ord(word[i])<=ord('Z'):
                        return False
            else:
                for i in range(2,len(word)):
                    if ord(word[i])>ord('Z'):
                        return False
        return True
    
print(Solution().detectCapitalUse("FlaG"))