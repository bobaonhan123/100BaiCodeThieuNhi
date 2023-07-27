from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        mp=dict()
        words.sort()
        for i in words:
            if len(i)==1:
                mp[i]=0
            elif i[:-1] not in mp:
                mp[i]=-9999
            else:
                mp[i]=mp[i[:-1]]+1
        ma=0
        for i in mp:
            if mp[i]>ma:
                ma=mp[i]
        for i in words:
            if mp[i]==ma:
                return i
        return ""
print(Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))
