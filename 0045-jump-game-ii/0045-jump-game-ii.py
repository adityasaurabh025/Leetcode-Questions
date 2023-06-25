class Solution:
    def jump(self, nums: List[int]) -> int:
        
        curr_farthest = curr_end = jumps = 0 
        for i in range(len(nums)-1) :
            curr_farthest = max(curr_farthest, i + nums[i]) #max of the farthest elements that we can reach
            if i == curr_end : #we have exhausted all min paths that we can get 
                jumps += 1 #increment jumps to the next index
                curr_end = curr_farthest #update the current farthest element value in curr
        
        return jumps