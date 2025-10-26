# a -> ab -> abc -> abca -> bca -> bcab -> cab -> cabc -> abc -> abcb -> bcb -> cb -> cbb

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0    # 첫글자
        right = 0   # 마지막글자
        letters = set()
        answer = 0

        for right in range(len(s)):
            curr = s[right]

            # 중복 문자가 있는 경우
            while curr in letters:
                letters.remove(s[left])
                left += 1

            letters.add(curr)
            answer = max(right - left + 1, answer)
        
        return answer

