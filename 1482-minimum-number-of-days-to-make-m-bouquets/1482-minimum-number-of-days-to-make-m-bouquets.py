class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeB(D):
            bouquets=0
            flowers=0
            
            for bloom in bloomDay:
                if bloom<=D:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
            return bouquets>=m
        
        if len(bloomDay)<m*k:
            return -1
        
        left, right= min(bloomDay), max(bloomDay)
        
        while left<=right:
            mid = (left + right) // 2  # Calculate the middle point
            if canMakeB(mid):  # Check if we can make m bouquets by day mid
                right = mid - 1  # If yes, try to find an earlier valid day
            else:
                left = mid + 1
        return left if canMakeB(left) else -1