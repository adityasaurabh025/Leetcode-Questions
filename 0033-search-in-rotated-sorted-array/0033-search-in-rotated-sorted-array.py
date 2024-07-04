class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        return nums.index(target) if target in nums else -1
    
#         n= len(nums)
#         left=0
#         right=n-1
        
#         mid= ((right+left)//2)
        
#         while left<= right:
            
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]> target:
#                 left=mid+1
#             else:
#                 right= mid-1
        
#         return -1