
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s=set()
        for i in words:
            morsestr=""
            
            for j in range(len(i)):
                morsestr+=morse[ord(i[j])-ord('a')]
            if not morsestr in s:
                s.add(morsestr)
        return len(s)
print(Solution().uniqueMorseRepresentations(["gin","zen","gig","msg"]))