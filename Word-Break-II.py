class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        memo = {}  # Dictionary to store the results of subproblems
        
        def backtrack(start: int) -> List[str]:
            if start in memo:
                return memo[start]  # Return the cached result
            if start == len(s):
                return [""]  # End of the string, return an empty list

            results = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sentence in backtrack(end):
                        if sentence:
                            results.append(word + " " + sentence)
                        else:
                            results.append(word)
            memo[start] = results  # Cache the result
            return results

        return backtrack(0)

# Example usage
solution = Solution()
print(solution.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))  # Output: ["cats and dog","cat sand dog"]
print(solution.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))  # Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # Output: []
