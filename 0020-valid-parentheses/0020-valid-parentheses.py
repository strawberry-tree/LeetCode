class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {")": "(", "}": "{", "]": "["}
        stack = []
        for letter in s:
            if letter in ["(", "{", "["]:
                stack.append(letter)
            elif stack and par_dict[letter] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack 
