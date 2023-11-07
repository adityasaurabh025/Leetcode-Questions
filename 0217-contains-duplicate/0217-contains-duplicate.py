class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_list= nums.sort()
        length=len(nums)
        for num in range(length-1):
            if nums[num]==nums[num+1]:
                return True
        return False
        
        
        
         