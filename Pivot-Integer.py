class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        
        # Iterate through each integer from 1 to n
        for x in range(1, n + 1):
            left_sum = x * (x + 1) // 2
            right_sum = total_sum - left_sum + x
            
            # Check if left_sum equals right_sum
            if left_sum == right_sum:
                return x
        
        return -1

# Example usage:
solution = Solution()
print(solution.pivotInteger(8))  # Output: 6
print(solution.pivotInteger(1))  # Output: 1
print(solution.pivotInteger(4))  # Output: -1
