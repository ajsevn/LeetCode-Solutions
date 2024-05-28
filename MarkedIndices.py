import collections

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        count = 0
        num_count = collections.Counter(nums)
        nums.sort()  # Sort the list to find the smallest numbers first
        
        for i, num in enumerate(nums):
            j = i + 1
            while j < len(nums) and 2 * num > nums[j]:  # Find the smallest j where 2 * nums[i] <= nums[j]
                j += 1
                
            if j < len(nums):
                count += 2  # Mark both i and j
                num_count[num] -= 1
                num_count[nums[j]] -= 1
                
        return count

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3, 5, 2, 4]
    print(solution.maxNumOfMarkedIndices(nums1))  # Output: 2

    nums2 = [9, 2, 5, 4]
    print(solution.maxNumOfMarkedIndices(nums2))  # Output: 4

    nums3 = [7, 6, 8]
    print(solution.maxNumOfMarkedIndices(nums3))  # Output: 0
