class Solution:
        def maxProduct(self, nums: List[int])-> int:
            if not nums:
                return 0
            
            max_product=nums[0]
            curr_max=nums[0]
            curr_min= nums[0]
            
            
            for i in range(1, len(nums)):
                num= nums[i]
                
                if num < 0:
                    curr_max, curr_min= curr_min, curr_max
                
                curr_max= max(num, num*curr_max)
                curr_min= min(num, num*curr_min)
                
                max_product= max(max_product, curr_max)
                
            return max_product
            
"""
When dealing with the product of subarrays, negative numbers can drastically change the maximum and minimum products:

Multiplying a large positive number by a negative number makes it negative.
Multiplying a large negative number by a negative number makes it positive.
Thus, at each step, the maximum product can become the minimum product and vice versa when a negative number is encountered. By swapping curr_max and curr_min when a negative number is encountered, we ensure that we correctly keep track of both the potential maximum and minimum products.

Consider the array nums = [2, 3, -2, 4].

Initialization:

max_product = 2
curr_max = 2
curr_min = 2
Iteration over the array:

Index 1 (num = 3):

num = 3
if num < 0:  # False, so no swap
curr_max = max(3, 2 * 3) = 6
curr_min = min(3, 2 * 3) = 3
max_product = max(2, 6) = 6


Index 2 (num = -2):

num = -2
if num < 0:  # True, so swap curr_max and curr_min
curr_max, curr_min = curr_min, curr_max  # curr_max = 3, curr_min = 6
curr_max = max(-2, 3 * -2) = -2
curr_min = min(-2, 6 * -2) = -12
max_product = max(6, -2) = 6


Index 3 (num = 4):

num = 4
if num < 0:  # False, so no swap
curr_max = max(4, -2 * 4) = 4
curr_min = min(4, -12 * 4) = -48
max_product = max(6, 4) = 6

"""

            
        