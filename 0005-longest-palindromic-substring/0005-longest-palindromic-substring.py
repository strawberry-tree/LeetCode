from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            
        answer = s[0]
        for i in range(len(s) - 1):
            answer = max(answer, check(i, i + 1), check(i, i + 2), key=len)

        return answer 
            


