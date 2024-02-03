class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:]= [num for num in nums if num!=val]
        return len(nums)
#         n=len(nums)
#         k=0
        
#         for i in range(n):
#             if nums[i]!=val:
#                 nums[k]=nums[i]
#                 k+=1
#         return k

