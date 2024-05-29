import math
from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if math.gcd(nums[i], nums[j]) > 1:
                    uf.union(i, j)
        
        root = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != root:
                return False
        return True

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [2, 3, 6]
    print(solution.canTraverseAllPairs(nums1))  # Output: True

    nums2 = [3, 9, 5]
    print(solution.canTraverseAllPairs(nums2))  # Output: False

    nums3 = [4, 3, 12, 8]
    print(solution.canTraverseAllPairs(nums3))  # Output: True
