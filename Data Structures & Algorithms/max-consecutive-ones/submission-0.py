class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        aux = 0
        max_conseq = 0
        for i in range(n):
            if nums[i] == 1:
                aux += 1
            else:
                max_conseq = max(max_conseq, aux)
                aux = 0
        return max(max_conseq, aux)
        

    
