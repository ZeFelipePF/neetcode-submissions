class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > matrix[mid][-1]:
                L = mid + 1
            else:
                R = mid -1
        
        if L == len(matrix):
            return False


        arr = matrix[L]

        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if arr[mid] > target:
                R = mid - 1
            elif arr[mid] < target:
                L = mid + 1
            else:
                return True

        return False