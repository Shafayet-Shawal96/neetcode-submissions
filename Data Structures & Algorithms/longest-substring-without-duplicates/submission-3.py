class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        hashTable = [0]*95
        result = 0

        for c in s:
            charIndex = ord(c)-32

            if hashTable[charIndex] == 1:
                while hashTable[charIndex] == 1:
                    pop = window.pop(0)
                    popIndex = ord(pop)-32
                    hashTable[popIndex] = 0
            window.append(c)
            hashTable[charIndex] = 1
            result = max(result,len(window))
                

        return result
            
