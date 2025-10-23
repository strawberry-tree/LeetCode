class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs = []
        digit_logs = []

        for log in logs:
            [identifier, *rest] = log.split()
            rest = " ".join(rest)
            if rest[0].isalpha():
                letter_logs.append([identifier, rest])
            else:
                digit_logs.append([identifier, rest])

        

        # content -> identifier 순으로 order
        letter_logs.sort(key = lambda x: (x[1], x[0]))
        result = []
        for log in letter_logs:
            result.append(f"{log[0]} {log[1]}")
        for log in digit_logs:
            result.append(f"{log[0]} {log[1]}")

        return result