class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if parent[x]!=x:
                parent[x]= find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX=find(x)
            rootY= find(y)
            if rootX!= rootY:
                parent[rootY]=rootX
        n= len(isConnected)
        parent= list(range(n))
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]==1:
                    union(i, j)
        province= len(set(find(i) for i in range(n)))
        return province

        
        
        
        
        
#         def dfs(i):
#             for j in range(len(isConnected)):
#                 if isConnected[i][j]==1 and not visited[j]:
#                     visited[j]= True
#                     dfs(j)
        
#         n= len(isConnected)
#         visited = [False]* n
        
#         province=0
        
#         for i in range(n):
#             if not visited[i]:
#                 dfs(i)
#                 province+=1
#         return province

