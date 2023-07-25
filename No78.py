from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i)>ord(target):
                return i
        return letters[0]
print(Solution().nextGreatestLetter(["c","f","j"], "a"))