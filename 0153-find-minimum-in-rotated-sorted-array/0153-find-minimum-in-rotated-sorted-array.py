class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left, right=0, n-1
            
        
        while left<right:
            mid= (left+right)//2
            if nums[mid]> nums[right]:
                left= mid+1
            else:
                right=mid
        return nums[left]
        
#         mini= nums[0]
        # TC: O(n)
#         for i in range(len(nums)):
#             if nums[i]< mini:
#                 mini=nums[i]
#         return mini
"""
For the array [4,5,6,7,0,1,2]:

Initial left = 0, right = 6, mid = 3:
nums[mid] = 7, nums[right] = 2:
Since nums[mid] > nums[right], set left = mid + 1 = 4.
Now, left = 4, right = 6, mid = 5:
nums[mid] = 1, nums[right] = 2:
Since nums[mid] <= nums[right], set right = mid = 5.
Now, left = 4, right = 5, mid = 4:
nums[mid] = 0, nums[right] = 1:
Since nums[mid] <= nums[right], set right = mid = 4.
Now, left = 4, right = 4:
The loop terminates, and nums[left] = nums[4] = 0 is the minimum element.
This approach ensures that the solution runs in 
\U0001d442(log\U0001d45b)
O(logn) time, making it efficient for large arrays.
"""
          
          
        
        