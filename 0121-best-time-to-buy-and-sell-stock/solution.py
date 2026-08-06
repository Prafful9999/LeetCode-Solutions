class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxi = len(prices)-1
        mini = len(prices)-2
        while mini >=0:
            diff = prices[maxi]-prices[mini]
            profit = max(diff,profit)
            if prices[maxi]-prices[mini] <0:
                maxi = mini
                mini = mini-1
            else:
                mini = mini-1
        return profit

            
        
            
        



        