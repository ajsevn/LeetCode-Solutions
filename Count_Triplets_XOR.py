class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        count = 0
        xor_map = {}
        
        for i in range(len(prefix_xor)):
            if prefix_xor[i] in xor_map:
                for prev_index in xor_map[prefix_xor[i]]:
                    count += (i - 1) - prev_index
                xor_map[prefix_xor[i]].append(i)
            else:
                xor_map[prefix_xor[i]] = [i]
        
        return count

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    arr1 = [2, 3, 1, 6, 7]
    print(solution.countTriplets(arr1))  # Output: 4

    arr2 = [1, 1, 1, 1, 1]
    print(solution.countTriplets(arr2))  # Output: 10
