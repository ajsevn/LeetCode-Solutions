class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all the numbers to get xor_all which is the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a set bit (1-bit) in xor_all
        # This can be done using xor_all & -xor_all to get the rightmost set bit
        set_bit = xor_all & -xor_all
        
        # Step 3: Partition the numbers into two groups and XOR each group
        num1 = 0
        num2 = 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1, 2, 1, 3, 2, 5]
    print(solution.singleNumber(nums1))  # Output: [3, 5] or [5, 3]

    nums2 = [-1, 0]
    print(solution.singleNumber(nums2))  # Output: [-1, 0]

    nums3 = [0, 1]
    print(solution.singleNumber(nums3))  # Output: [0, 1]
