class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        # return nums.index(target) if target in nums else -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        # TC:- O(N)
    
       