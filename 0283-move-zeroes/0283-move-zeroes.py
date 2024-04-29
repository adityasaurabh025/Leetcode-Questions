class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        idx=0
        for i in range(len(nums)):
            if nums[i]!=0: # check all non-zero elements and add it in the array
                nums[idx]=nums[i] 
                idx+=1
        while idx < len(nums): #fill the array with zero untill idx reaches length of nums in the end
            nums[idx]=0
            idx+=1
            """
        zeroPos = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[cur], nums[zeroPos] = nums[zeroPos], nums[cur]
                zeroPos += 1