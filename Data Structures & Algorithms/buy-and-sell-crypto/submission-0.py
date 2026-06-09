class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        mp = 0

        while s<len(prices):
            if prices[b] < prices[s]:
                profit = prices[s]-prices[b]
                mp = max(mp, profit)
            else:
                b = s
            
            s+=1

        return mp