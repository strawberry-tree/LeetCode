class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ordered_s = sorted(list(s))
        ordered_t = sorted(list(t))
        return ordered_s == ordered_t