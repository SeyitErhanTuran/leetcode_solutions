class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            found_unique = True
            for j in range(n):
                if i !=j and s[i] == s[j]:
                    found_unique = False
                    break
            if found_unique:
                return i
        return -1
        
solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))
print(solution.firstUniqChar("aabb"))