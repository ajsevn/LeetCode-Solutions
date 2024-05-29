from typing import List
import math
from collections import defaultdict

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

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        uf = UnionFind(n)
        prime_to_indices = defaultdict(list)

        # Collect indices for each prime factor
        for i, num in enumerate(nums):
            for factor in prime_factors(num):
                prime_to_indices[factor].append(i)

        # Union indices that share a prime factor
        for indices in prime_to_indices.values():
            for i in range(1, len(indices)):
                uf.union(indices[0], indices[i])

        # Check if all indices are connected
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
