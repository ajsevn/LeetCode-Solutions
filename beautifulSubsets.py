class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Initialize the result counter to 0
        self.result = 0

        # Backtracking function to explore all subsets
        def backtrack(start, current_set):
            # Add the current subset to the result
            if current_set:
                self.result += 1
            
            # Explore further elements to add to the current subset
            for i in range(start, len(nums)):
                # Check if the current element can be added to the subset
                can_add = True
                for num in current_set:
                    if abs(nums[i] - num) == k:
                        can_add = False
                        break
                
                # If the element can be added, continue exploring with this element included
                if can_add:
                    current_set.append(nums[i])
                    backtrack(i + 1, current_set)
                    current_set.pop()

        # Sort the numbers to avoid redundant checks
        nums.sort()
        # Start the backtracking process from the first element
        backtrack(0, [])
        return self.result

# Example usage:
solution = Solution()
print(solution.beautifulSubsets([2, 4, 6], 2))  # Output: 4
print(solution.beautifulSubsets([1], 1))       # Output: 1
