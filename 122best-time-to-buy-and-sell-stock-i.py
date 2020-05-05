class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        pre_p = prices[0]
        for p in prices[1:]:
            if p > pre_p:
                profit += p - pre_p
            pre_p = p
        return profit
