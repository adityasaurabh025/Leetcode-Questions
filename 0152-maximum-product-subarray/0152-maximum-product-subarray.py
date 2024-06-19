class Solution:
        def maxProduct(self, nums: List[int])-> int:
            if not nums:
                return 0
        
        # Initialize variables to track the maximum product, the current maximum and minimum product
            max_product = nums[0]
            curr_max = nums[0]
            curr_min = nums[0]
        
            for i in range(1, len(nums)):
                num = nums[i]
            
                if num < 0:
                    curr_max, curr_min = curr_min, curr_max
            
                curr_max = max(num, curr_max * num)
                curr_min = min(num, curr_min * num)
            
                max_product = max(max_product, curr_max)
        
            return max_product
            
#             n= len(nums)
#             mxm= 0
#             curr_max=0
            
#             left=nums[0]
#             right= nums[1]
#             for i in range(1,n):
#                 mxm =left*right
#                 if mxm> curr_max:
#                     curr_max=mxm
#                     right+=1
#                 else:
#                     left+=1
#             return curr_max

            
        