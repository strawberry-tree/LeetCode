class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2letter = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result = []

        def check(digits, idx, curr):
            if idx >= len(digits):
                result.append(curr)
                return

            for letter in num2letter[int(digits[idx])]:
                check(digits, idx + 1, curr + letter)

        check(digits, 0, "")
        return result
            