class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use Two pointer and keep track of max profit
        # left=0
        # right=1
        # max_profit_so_far=0
        # while right<len(prices):
        #     current_profit=prices[right]-prices[left]
        #     if prices[right]> prices[left]:
        #         max_profit_so_far= max(current_profit, max_profit_so_far)
        #     else:
        #         left=right
        #     right+=1
        # return max_profit_so_far
        
        
        #using DP
        if not prices:
            return 0
        max_profit=0
        min_price=prices[0]
        
        for i in range(1, len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                max_profit= max(max_profit, prices[i]-min_price)
        return max_profit

                