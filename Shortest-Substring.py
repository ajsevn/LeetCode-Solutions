from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        # Function to generate all possible substrings of a given string
        def generate_substrings(s):
            substrings = set()
            length = len(s)
            for i in range(length):
                for j in range(i + 1, length + 1):
                    substrings.add(s[i:j])
            return substrings
        
        # Step 1: Generate all substrings for each string and store their occurrences
        substring_count = defaultdict(int)
        string_substrings = []
        
        for string in arr:
            substrings = generate_substrings(string)
            string_substrings.append(substrings)
            for substring in substrings:
                substring_count[substring] += 1
        
        # Step 2: Determine the shortest unique substring for each string
        answer = []
        
        for i, string in enumerate(arr):
            unique_substrings = [sub for sub in string_substrings[i] if substring_count[sub] == 1]
            if not unique_substrings:
                answer.append("")
            else:
                answer.append(min(unique_substrings, key=lambda x: (len(x), x)))
        
        return answer

# Example usage
sol = Solution()
arr1 = ["cab", "ad", "bad", "c"]
arr2 = ["abc", "bcd", "abcd"]
print(sol.shortestSubstrings(arr1))  # Output: ["ab", "", "ba", ""]
print(sol.shortestSubstrings(arr2))  # Output: ["", "", "abcd"]
