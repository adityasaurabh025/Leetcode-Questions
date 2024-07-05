class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        # if n==1:
        #     return 0
        # return nums.index(max(nums))
        # TC- O(n), SC- O(1)
        
        low, high= 0, n-1
        
        while low < high:
            mid= (low+high)//2
            
            if nums[mid]< nums[mid+1]:
                low=mid+1 # If mid element is less, the peak is in the right half.
            else:
                high= mid # If mid element is greater, the peak is in the left half.
        return low
                
        
        
    