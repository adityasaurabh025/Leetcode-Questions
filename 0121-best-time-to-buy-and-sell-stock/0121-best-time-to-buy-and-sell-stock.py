class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use Two pointer and keep track of max profit
        left=0
        right=1
        max_profit_so_far=0
        while right<len(prices):
            current_profit=prices[right]-prices[left]
            if prices[right]> prices[left]:
                max_profit_so_far= max(current_profit, max_profit_so_far)
            else:
                left=right
            right+=1
        return max_profit_so_far
    
    
#     class Solution:
#     def maxProfit(self,prices):
#         left = 0 #Buy
#         right = 1 #Sell
#         max_profit = 0
#         while right < len(prices):
#             currentProfit = prices[right] - prices[left] #our current Profit
#             if prices[left] < prices[right]:
#                 max_profit =max(currentProfit,max_profit)
#             else:
#                 left = right
#             right += 1
#         return max_profit
                