class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[[*s],[*t]]
        arr[0].sort()
        arr[1].sort()
        return ''.join(arr[0])==''.join(arr[1])
print(Solution().isAnagram("anagram","nagaram"))