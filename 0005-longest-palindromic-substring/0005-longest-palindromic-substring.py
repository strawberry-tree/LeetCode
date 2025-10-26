from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = defaultdict(list)
        N = len(s)
        answer = ""

        for i in range(N):
            window = 0

            while 0 <= i - window and i + window < N:
                if s[i - window] != s[i + window]:
                    break
                window += 1
  
            window -= 1
            
            if window >= 0 and 1 + 2 * window > len(answer):
                print(answer, s[i-window:i+window+1])
                answer = s[i - window:i+window + 1]

        for i in range(N - 1):
            window = 0
            while 0 <= i - window and i + window + 1 < N:
                if s[i - window] != s[i + window + 1]:
                    break
                window += 1
            window -= 1

            if window >= 0 and 2 * window + 2 > len(answer):
                print(answer, s[i-window:i+window+2])
                answer = s[i - window: i+ window + 2]

        return answer 
            


