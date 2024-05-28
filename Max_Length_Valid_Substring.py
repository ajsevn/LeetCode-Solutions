class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0
        current_cost = 0
        max_length = 0
        
        for right in range(n):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example usage
solution = Solution()
print(solution.equalSubstring("abcd", "bcdf", 3))  # Output: 3
print(solution.equalSubstring("abcd", "cdef", 3))  # Output: 1
print(solution.equalSubstring("abcd", "acde", 0))  # Output: 1
