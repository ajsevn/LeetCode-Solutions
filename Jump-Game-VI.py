from collections import deque

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])  # store indices of `dp` array, and maintain decreasing order of `dp` values
        
        for i in range(1, n):
            # Remove elements from the front that are out of the window of the last k steps
            while dq and dq[0] < i - k:
                dq.popleft()
            
            # dp[i] is the sum of nums[i] and the max value within the last k steps
            dp[i] = nums[i] + dp[dq[0]]
            
            # Maintain deque in decreasing order of `dp` values
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            # Add current index to the deque
            dq.append(i)
        
        # The result is the max score to reach the last index
        return dp[-1]

# Example usage
sol = Solution()
print(sol.maxResult([1,-1,-2,4,-7,3], 2))  # Output: 7
print(sol.maxResult([10,-5,-2,4,0,3], 3))  # Output: 17
print(sol.maxResult([1,-5,-20,4,-1,3,-6,-3], 2))  # Output: 0
