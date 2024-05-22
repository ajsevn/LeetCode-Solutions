class Solution:
    def subsets(self, nums):
        result = []
        
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return result

# Example usage:
solution = Solution()
print(solution.subsets([1, 2, 3]))  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(solution.subsets([0]))        # Output: [[], [0]]
