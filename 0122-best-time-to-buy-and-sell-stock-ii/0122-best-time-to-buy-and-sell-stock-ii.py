class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=max_sum_of_stock=0
        n=len(prices)
        
        for i in range(1,n):
            if(prices[i-1]<prices[i]):
                max_sum_of_stock+=prices[i]-prices[i-1]
                
        return max_sum_of_stock