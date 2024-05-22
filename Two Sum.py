class Solution:
    def twoSum(self, nums, target):
        # Initialize a dictionary to store the indices of numbers we have seen
        num_to_index = {}
        
        # Iterate over the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the current number and its complement
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index

        # If no solution is found (though the problem guarantees one), raise an exception
        raise ValueError("No two sum solution exists")

# Example usage:
# This part should not be included when submitting to LeetCode, 
# but is here for local testing.
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
