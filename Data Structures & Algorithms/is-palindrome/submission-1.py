class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            asci = ord(c)
            if (asci > 47 and asci <58) or (asci > 64 and asci <91) or (asci > 96 and asci <123):
                newStr = newStr + c.lower()
        
        l = 0
        r = len(newStr) - 1
        while l<r:
            if newStr[l] != newStr[r]:
                return False
            l = l+1
            r = r-1

        return True