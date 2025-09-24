# LeetCode #1: Two Sum
# Brute force: O(n^2)
# HashMap: O(n)

from typing import List


class Solution:
     def twoSumBruteForce(self, nums: List[int], target:int) -> List[int]:
          for i in range(len(nums)):
               for j in range(i+1, len(nums)):
                    current_sum = nums[i] + nums[j]
                    if current_sum == target:
                         return [i, j]
    
     def twoSumHashMap(self, nums: List[int], target:int) -> List[int]:
          seen = {}
          for i, num in enumerate(nums):
               complement = target - num
               if complement in seen:
                    return [seen[complement], i]
               else:
                    seen[num] = i




solution = Solution()
print(solution.twoSumHashMap([2, 7, 11, 15], 9))
 


