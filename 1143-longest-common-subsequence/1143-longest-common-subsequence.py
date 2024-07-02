class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m= len(text1)+1
        n= len(text2)+1
        
        dp=[[0]* (n) for _ in range(m)] # fill zero in array
        
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1] # if chars are matching, increase the count and decrease the pointers
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])# if array is not match then take max of both observations
        return dp[-1][-1] # return -1 if not present