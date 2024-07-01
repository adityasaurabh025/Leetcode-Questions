class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n= len(nums)
       # since size of array is fixed we can count the ocurance and then adjust the array based on count
        count_0=0
        count_1=0
        count_2=0
        
        for num in nums:
            if num==0:
                count_0+=1
            elif num==1:
                count_1+=1
            elif num==2:
                count_2+=1
            
        nums[:count_0]=[0]* count_0
        nums[count_0: count_0+count_1]=[1]* count_1
        nums[count_0+count_1:]=[2]*count_2
        
        return nums
                
                
                
                
                
#         temp=nums
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i]>nums[j]:
#                     temp=nums[i]
#                     nums[i]=nums[j]
#                     nums[j]=temp
                    
#         return temp

        