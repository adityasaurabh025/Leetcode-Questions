class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # To handle cases where k > n
        reverseArr(nums, 0, n-1) # reverse entire array
        reverseArr(nums, 0, k-1) # reverse first k elements from start
        reverseArr(nums, k, n-1) # reverse remaining elements from k till end
        
def reverseArr(nums, start, end ):
    while start< end:
        nums[start], nums[end]= nums[end], nums[start]
        start+=1
        end-=1
        
        
#     # Rotate the array in-place using slicing
#         nums[:] = nums[-k:] + nums[:-k]
            
        
        