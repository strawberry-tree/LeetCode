import re

class Solution:
    results = []

    def diffWaysToCompute(self, expression: str) -> List[int]:

        def check(num_list, exp_list):
            if len(num_list) == 1 and len(exp_list) == 0:
                return num_list
            
            results = []
            for mid in range(len(exp_list)):
                left = check(num_list[:mid + 1], exp_list[:mid])
                action = exp_list[mid]
                right = check(num_list[mid+1:], exp_list[mid + 1:])

                for lv in left:
                    for rv in right:
                        if action == "+":
                            results.append(lv + rv)
                        elif action == "-":
                            results.append(lv - rv)
                        elif action == "*":
                            results.append(lv * rv)
            return results

        num_list = []
        exp_list = []
        curr = ""
        for letter in expression:
            if letter in ["+", "-", "*"]:
                num_list.append(int(curr))
                exp_list.append(letter)
                curr = ""
            else:
                curr += letter
        num_list.append(int(curr))
        
        return check(num_list, exp_list)