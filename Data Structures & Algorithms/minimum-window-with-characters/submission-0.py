class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = 1+tMap.get(c,0)

        windowMap = {}
        result = ""
        l,r=0,0

        have = 0
        need = len(tMap)

        while r<len(s):
            c = s[r]
            windowMap[c] = 1+windowMap.get(c,0)

            if c in tMap and windowMap[c] == tMap[c]:
                have+=1

                while have==need:
                    if result == "" or len(result)>r-l+1:
                        result = s[l:r+1]

                    g = s[l]
                    windowMap[g] -= 1
                    if g in tMap and windowMap[g] < tMap[g]:
                        have-=1

                    l+=1

            r+=1
        return result





                

