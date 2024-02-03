class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged= nums1 + nums2
        
        merged.sort()
        
        total_len=len(merged)
        
        if total_len%2==1:
            return float(merged[total_len//2])
        else:
            median1= merged[total_len//2-1]
            median2= merged[total_len//2]
            return float((median1 + median2)/2.0)