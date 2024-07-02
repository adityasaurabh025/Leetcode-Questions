class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        n=len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
    
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
        return dp[-1]
        
#         prev1 = max(nums[0], nums[1])
#         prev2 = nums[0]
#         n=len(nums)
#         for i in range(2, n):
#             current = max(nums[i] + prev2, prev1)
#             prev2 = prev1
#             prev1 = current
    
#         return prev1
    
    """
    Calculate current:

current = max(nums[i] + prev2, prev1)
This line calculates the maximum amount of money that can be robbed if we consider the current house (nums[i]).
There are two choices:
Rob the current house and add its money to the maximum amount robbed up to two houses before (nums[i] + prev2).
Skip the current house and keep the maximum amount robbed up to the previous house (prev1).
Update prev2:

prev2 = prev1
Move the prev1 value to prev2 because in the next iteration, prev1 will represent the previous house.
Update prev1:

prev1 = current
The current value becomes the new prev1, representing the maximum amount of money robbed up to the current house.
    """
    
    
#         prev1=max(nums[1], nums[0]) # Robber can select which house to loot first, either first or second based on max loot amount
#         prev2= nums[0] #Robber is standing at first house
#         n= len(nums)
#         for num in range(2, n):
#             current=max(num+prev2, prev1)
#             prev2= prev1
#             prev1=current
        
#         return prev1
        
                