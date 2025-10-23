class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_list = [lett.lower() for lett in s if lett.isalpha() or lett.isdigit()]
        return alpha_list == alpha_list[::-1]
        