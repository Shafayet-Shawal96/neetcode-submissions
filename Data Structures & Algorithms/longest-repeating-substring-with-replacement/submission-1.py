class Solution:
    def maxCount(self, counts: [int])-> int:
        result = 0
        for c in counts:
            result = max(result,c)
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0]*26
        l,r = 0,0
        result = 0

        while r<len(s):
            rCharIndex = ord(s[r])-65
            counts[rCharIndex]+=1
            mostCount = self.maxCount(counts)
            if r-l+1 - mostCount <=k:
                result = max(result, r-l+1)
            else:
                lCharIndex = ord(s[l])-65
                counts[lCharIndex]-=1
                l+=1
            r+=1

        return result