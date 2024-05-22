class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        left, right = 0, n - 1
        total_chemistry = 0
        target_sum = skill[left] + skill[right]
        
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return total_chemistry

# Example usage:
solution = Solution()
print(solution.dividePlayers([3, 2, 5, 1, 3, 4]))  # Output: 22
print(solution.dividePlayers([3, 4]))              # Output: 12
print(solution.dividePlayers([1, 1, 2, 3]))        # Output: -1
