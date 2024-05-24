class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        # Function to calculate the intersection of two rectangles
        def getIntersection(r1, r2):
            x1 = max(r1[0][0], r2[0][0])
            y1 = max(r1[0][1], r2[0][1])
            x2 = min(r1[1][0], r2[1][0])
            y2 = min(r1[1][1], r2[1][1])
            
            if x1 < x2 and y1 < y2:
                return (x1, y1, x2, y2)
            else:
                return None

        n = len(bottomLeft)
        max_side_length = 0
        
        # Check intersections for all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                intersection = getIntersection((bottomLeft[i], topRight[i]), (bottomLeft[j], topRight[j]))
                
                if intersection:
                    x1, y1, x2, y2 = intersection
                    side_length = min(x2 - x1, y2 - y1)
                    max_side_length = max(max_side_length, side_length)
        
        return max_side_length * max_side_length

# Example usage
sol = Solution()
bottomLeft1 = [[1,1],[2,2],[3,1]]
topRight1 = [[3,3],[4,4],[6,6]]
print(sol.largestSquareArea(bottomLeft1, topRight1))  # Output: 1

bottomLeft2 = [[1,1],[2,2],[1,2]]
topRight2 = [[3,3],[4,4],[3,4]]
print(sol.largestSquareArea(bottomLeft2, topRight2))  # Output: 1

bottomLeft3 = [[1,1],[3,3],[3,1]]
topRight3 = [[2,2],[4,4],[4,2]]
print(sol.largestSquareArea(bottomLeft3, topRight3))  # Output: 0
