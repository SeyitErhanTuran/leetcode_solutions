from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        arr = []

        while nums:
            
            alice = min(nums)
            nums.remove(alice)
            
            bob = min(nums)
            nums.remove(bob)

            arr.append(bob)
            arr.append(alice)
        
        return arr
    
solution = Solution()
print(solution.numberGame([5,4,2,3]))    
print(solution.numberGame([2,5]))    

