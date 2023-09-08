class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 0
        days = len(prices)
        while(buy < days and sell < days):
            while ( buy < days-1  and  prices[buy + 1] <= prices[buy]):
                buy += 1
            sell = buy
            while ( sell < days -1 and prices[sell + 1] >= prices[sell]):
                sell += 1
            profit += prices[sell] - prices[buy]
            buy = sell + 1
        return profit