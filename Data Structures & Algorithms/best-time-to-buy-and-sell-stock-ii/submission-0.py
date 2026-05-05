class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought_at = 0
        bought = False
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1] and bought:
                profit += (prices[i] - bought_at)
                bought = False
                print('SELL:', bought_at)
            elif prices[i] < prices[i + 1] and not bought:
                bought_at = prices[i]
                bought = True
                print('BUY:', bought_at)

        if bought:
            profit += (prices[i+1] - bought_at)
        return profit
