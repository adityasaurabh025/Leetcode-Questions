class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # To handle cases where k > n
    
    # Rotate the array in-place using slicing
        nums[:] = nums[-k:] + nums[:-k]
            
        
        