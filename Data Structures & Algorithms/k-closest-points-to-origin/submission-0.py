class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for point in points:
            dist = point[0]**2 + point[1]**2  # No sqrt needed!
            tupple = (dist, point)
            arr.append(tupple)

        arr.sort(key=lambda x: x[0])

        return [point for dist, point in arr[:k]]

        
