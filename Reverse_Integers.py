class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of x
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        # Reverse the digits
        reversed_x = int(str(x_abs)[::-1])
        
        # Apply the sign
        reversed_x *= sign
        
        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        return reversed_x

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    x1 = 123
    print(solution.reverse(x1))  # Output: 321

    x2 = -123
    print(solution.reverse(x2))  # Output: -321

    x3 = 120
    print(solution.reverse(x3))  # Output: 21
