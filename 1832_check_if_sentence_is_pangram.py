class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch not in sentence:
                return False
        return True    
    
solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(solution.checkIfPangram("leetcode"))
