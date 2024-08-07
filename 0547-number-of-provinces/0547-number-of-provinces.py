class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and not visited[j]:
                    visited[j]= True
                    dfs(j)
        
        n= len(isConnected)
        visited = [False]* n
        
        province=0
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                province+=1
        return province