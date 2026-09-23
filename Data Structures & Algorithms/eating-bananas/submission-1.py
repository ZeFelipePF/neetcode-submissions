class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)          

        while lo < hi:                  
            k = (lo + hi) // 2           

            hours = 0
            for p in piles:
                hours += (p + k - 1) // k   

            if hours <= h:
                hi = k                   
            else:
                lo = k + 1               
        return lo
            
