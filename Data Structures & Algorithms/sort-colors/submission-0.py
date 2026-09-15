class Solution:
    def bucketsort(self, arr: List[int]) -> List[int]:
        count = [0, 0, 0] #Crio o Array

        for n in arr:
            count[n] += 1

        i = 0

        for n in range(len(count)):
            for j in range(count[n]):
                arr[i] = n
                i += 1
            
        return arr


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.bucketsort(nums)
        