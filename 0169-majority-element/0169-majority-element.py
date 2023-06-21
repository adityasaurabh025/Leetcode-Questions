class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #sort the elements 
        return nums[(len(nums))//2] #If number is present more than n/2 times then it will be present at n/2
            
        