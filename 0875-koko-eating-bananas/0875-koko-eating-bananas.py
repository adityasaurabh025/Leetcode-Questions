class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish_in_time(K):
            hours = 0
            for bananas in piles:
                hours += (bananas + K - 1) // K  # ceiling division of bananas / K
            return hours <= h
    
        low, high = 1, max(piles)
    
        while low <= high:
            mid = (low + high) // 2
            if can_finish_in_time(mid):
                high = mid - 1
            else:
                low = mid + 1
    
        return low