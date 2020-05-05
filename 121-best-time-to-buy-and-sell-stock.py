class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
                continue
            if prices[i] -buy_price > profit:
                profit = prices[i] - buy_price
        return profit
