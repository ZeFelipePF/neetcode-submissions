class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            aux = 0
            for k in range(i+1, len(arr)):
                if arr[k] > aux:
                    aux = arr[k]
            arr[i] = aux

        arr[-1] = -1

        return arr