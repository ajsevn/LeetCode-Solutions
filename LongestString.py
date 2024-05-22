class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        longest = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            longest = max(longest, end - start + 1)
        
        return longest

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
