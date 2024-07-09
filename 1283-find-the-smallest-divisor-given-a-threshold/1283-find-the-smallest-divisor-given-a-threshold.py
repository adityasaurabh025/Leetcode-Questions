class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums:
            return -1
        
        if threshold < 0:
            return -1
        
        if any(num < 0 for num in nums):
            return -1
        
        start = 1
        end = max(nums)
        ans = -1
        while start<=end:
            mid = (start+end)//2
            sum = 0
            for ele in nums:
                sum += math.ceil(ele/mid)
            if sum <= threshold:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
            # print(mid,start,end)
        return ans
        
        
        
        
        
        
        
        
        
        
        """
        
        # Handle edge cases
    if not nums:
        return -1  # Indicate invalid input due to empty array
    
    if threshold <= 0:
        return -1  # Indicate invalid input due to non-positive threshold
    
    if any(num < 0 for num in nums):
        return -1  # Indicate invalid input due to negative numbers in the array

    # Start with the smallest possible divisor
    divisor = 1

    # Continue searching for the smallest valid divisor
    while True:
        # Calculate the total sum of the division results for the current divisor
        total_sum = 0
        for num in nums:
            # Divide each number by the divisor and round up to the nearest integer
            division_result = math.ceil(num / divisor)
            # Add the result to the total sum
            total_sum += division_result

        # Check if the total sum is less than or equal to the threshold
        if total_sum <= threshold:
            # If it is, we have found the smallest valid divisor
            return divisor

        # If not, try the next larger divisor
        divisor += 1# Handle edge cases
    if not nums:
        return -1  # Indicate invalid input due to empty array
    
    if threshold <= 0:
        return -1  # Indicate invalid input due to non-positive threshold
    
    if any(num < 0 for num in nums):
        return -1  # Indicate invalid input due to negative numbers in the array

    # Start with the smallest possible divisor
    divisor = 1

    # Continue searching for the smallest valid divisor
    while True:
        # Calculate the total sum of the division results for the current divisor
        total_sum = 0
        for num in nums:
            # Divide each number by the divisor and round up to the nearest integer
            division_result = math.ceil(num / divisor)
            # Add the result to the total sum
            total_sum += division_result

        # Check if the total sum is less than or equal to the threshold
        if total_sum <= threshold:
            # If it is, we have found the smallest valid divisor
            return divisor

        # If not, try the next larger divisor
        divisor += 1
        """