class Solution:
    def minTimeToVisitAllPoints(self, points):
        def distance(p1, p2):
            return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

        total_time = 0
        for i in range(1, len(points)):
            total_time += distance(points[i-1], points[i])

        return total_time

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    points1 = [[1,1],[3,4],[-1,0]]
    print(solution.minTimeToVisitAllPoints(points1))  # Output: 7

    points2 = [[3,2],[-2,2]]
    print(solution.minTimeToVisitAllPoints(points2))  # Output: 5
