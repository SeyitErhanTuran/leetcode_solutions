"""
LeetCode 258 - Add Digits
- addDigitsMathematical: O(1) digital root solution
- addDigitsString: O(log n) iterative solution
"""

class Solution:
    def addDigitsMathematical(self, num: int) -> int:    
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
    
    def addDigitsString(self, num: int) -> int:
        if num < 10:
            return num
        
        while num >= 10:
            s = 0
            s = sum(int(c) for c in str(num))
            num = s
        return num   


solution = Solution()
print(solution.addDigitsMathematical(38))
print(solution.addDigitsString(38))