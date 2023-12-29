class Solution:
    def jump(self, nums: List[int]) -> int:
        
#         jumps=max_reach=curr_ele=0
        
#         for i in range(len(nums)-1):
#             max_reach=max(max_reach, nums[i]+i)
#             if i==curr_ele:
#                 jumps+=1
#                 curr_ele=max_reach
#         return jumps
    
#https://www.youtube.com/watch?v=wLPdkLM_BWo&t=446s&ab_channel=CodewithAlisha
    
#BFS approach
        l=r=res=0
        farthest=0
        while r< len(nums)-1:
            
            for i in range(l, r+1):
                farthest=max(farthest, nums[i]+i)
            l=r+1
            r=farthest
            res+=1
        return res
    