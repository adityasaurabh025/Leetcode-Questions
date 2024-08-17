class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # Initialize DP array
        prev = [-1] * n  # To track the previous index

        max_index = 0  # Index of the largest element in the subset

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                if dp[i] > dp[max_index]:
                    max_index = i

    # Reconstruct the largest subset
        largest_subset = []
        while max_index >= 0:
            largest_subset.append(nums[max_index])
            max_index = prev[max_index]

        return largest_subset[::-1]
        