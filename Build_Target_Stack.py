class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        current = 1
        
        for num in target:
            while current < num:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1
        
        return result

# Example usage:
solution = Solution()
print(solution.buildArray([1, 3], 3))  # Output: ["Push", "Push", "Pop", "Push"]
print(solution.buildArray([1, 2, 3], 3))  # Output: ["Push", "Push", "Push"]
print(solution.buildArray([1, 2], 4))  # Output: ["Push", "Push"]
