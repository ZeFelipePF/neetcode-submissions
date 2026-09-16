class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0

        while i < len(matrix) - 1:
            if target > matrix[i][-1]:
                i += 1
            else: 
                break

        arr = matrix[i]

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