class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=float(inf)
        max_profit=0
        for i in prices:
            minimum=min(minimum,i)
            profit=i-minimum
            max_profit=max(max_profit,profit)
        return max_profit

        