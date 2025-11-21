from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            word_count = len(sentence.split())
            if word_count > max_words:
                max_words = word_count
                 
        return max_words


solution = Solution()
print(solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]))