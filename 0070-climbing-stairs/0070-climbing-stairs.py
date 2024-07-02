class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        
        prev1=1
        prev2=1
        
        for i in range(2, n+1):
            curr=prev1+prev2 #create theree pointers, add prev two in current and assign to move ahead
            prev2=prev1
            prev1=curr
        
        return prev1
        
#         dp=[0]*(n+1)
#         dp[0]=1
#         dp[1]=1
        
#         for i in range(2, n+1):
#             dp[i]= dp[i-1]+ dp[i-2]
        
#         return dp[n]
#     #TC- O(n), SC- O(n)
    
    
    
    """
    dp[0] = 1: There is one way to stay at the ground (do nothing).
    dp[1] = 1: There is one way to reach the first step (one single step).
    
    n = 5
dp = [0, 0, 0, 0, 0, 0] (size n + 1)
Set dp[0] = 1 and dp[1] = 1
Now dp = [1, 1, 0, 0, 0, 0]
Iteration:

For i = 2:
dp[2] = dp[1] + dp[0] = 1 + 1 = 2
Now dp = [1, 1, 2, 0, 0, 0]
For i = 3:
dp[3] = dp[2] + dp[1] = 2 + 1 = 3
Now dp = [1, 1, 2, 3, 0, 0]
For i = 4:
dp[4] = dp[3] + dp[2] = 3 + 2 = 5
Now dp = [1, 1, 2, 3, 5, 0]
For i = 5:
dp[5] = dp[4] + dp[3] = 5 + 3 = 8
Now dp = [1, 1, 2, 3, 5, 8]
Result:

Return dp[5] which is 8
    
    """