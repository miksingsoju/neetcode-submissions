class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                if -prices[buy] + prices[sell] > 0:
                    profit.append(prices[sell] - prices[buy])
        if len(profit) == 0:
            return 0
        
        return(max(profit))





