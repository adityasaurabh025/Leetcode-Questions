class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        
        for i in range(len(nums1)):
            num= nums1[i]
            index_in_nums2 = nums2.index(num)
            next_greater=-1
            
            for j in range(index_in_nums2+1, len(nums2)):
                if nums2[j]> num:
                    next_greater= nums2[j]
                    break
            ans[i]= next_greater
        return ans
                    
        