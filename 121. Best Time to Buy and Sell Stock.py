class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        low = float('inf')  # need a random really high value for first comparison

        for i in prices:
            low = min(low, i)
            prof = i - low
            max_profit = max(max_profit, prof)

        return max_profit
