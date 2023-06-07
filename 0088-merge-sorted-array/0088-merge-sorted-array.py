class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # Index of last element in nums1
        j = n - 1  # Index of last element in nums2
        k = m + n - 1  # Index of last element in the merged array

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are any remaining elements in nums2, they should be copied to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1