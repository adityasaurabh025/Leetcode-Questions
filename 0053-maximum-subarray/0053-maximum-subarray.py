import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
#         maxi = -sys.maxsize - 1  # maximum sum
#         n= len(nums)
#         for i in range(n):
#             for j in range(i, n):
#             # subarray = arr[i.....j]
#                 summ = 0

#             # add all the elements of subarray:
#                 for k in range(i, j+1):
#                     summ += nums[k]

#                 maxi = max(maxi, summ)

#         return maxi
          