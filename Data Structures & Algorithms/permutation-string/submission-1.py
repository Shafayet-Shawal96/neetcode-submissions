class Solution:
    def charPosition(self, c):
        return ord(c)-ord('a')
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1CharCount = [0]*26

        for c in s1:
            position = self.charPosition(c)
            s1CharCount[position] += 1

        size = len(s1)
        l,r = 0,0
   
        for l in range(len(s2)):
            if s1CharCount[self.charPosition(s2[l])] != 0:
                if size == 1:
                    return True
                s1CountCopy = s1CharCount.copy()
                s1CountCopy[self.charPosition(s2[l])] -= 1
                r = l+1
                while r<len(s2):                   
                    if s1CountCopy[self.charPosition(s2[r])] != 0:
                        if r-l+1 == size:
                            return True
                        else:
                            s1CountCopy[self.charPosition(s2[r])] -= 1
                            r += 1
                    else:
                        l+=1
                        break
        
        return False

