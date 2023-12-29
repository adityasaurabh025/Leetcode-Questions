class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=nums[0] #Initialize maximum reachable element to first index
        
        for i in range(1, len(nums)): # Fhir index 1 se loop kro end tak
            if max_reach<i: # agar max_reach less that hai index se then false or can't reach
                return False
            else:
                max_reach=max(max_reach, nums[i]+i) #max_reach me max daal do curr max ka aur index aur element ko add krke jo aaye wo
        return True