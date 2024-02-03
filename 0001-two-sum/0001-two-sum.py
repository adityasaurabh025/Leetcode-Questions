class Solution:
    def twoSum(self, nums, target):
        
        #Brute Force
        # ans= [0,0]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]
        # TC:- O(n*2), SC:- O(1)
        
        #hashMap
        hashmap={}
        for i in range(len(nums)):
            diff= target-nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[nums[i]]=i
        # TC:- O(n), SC:- O(n)
        
        #Approach 3, sorting
        '''
        Sort the array.
Use two pointers approach - one starting from the beginning and the other from the end.
Move the pointers based on whether the sum is less than or greater than the target.
This approach has a time complexity of O(n log n) due to sorting and a space complexity of O(1).
        '''
        # nums_with_index = [(num, i) for i, num in enumerate(nums)]
        #nums_with_index.sort()
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        #     if current_sum == target:
        #         return [nums_with_index[left][1], nums_with_index[right][1]]
        #     elif current_sum < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []
        
        
        


