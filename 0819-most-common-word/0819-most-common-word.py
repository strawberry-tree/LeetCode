from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph)
        banned = set(banned)
        print(paragraph)

        words = [word.lower() for word in paragraph.split() if word.lower() not in banned]
        word_counts = Counter(words)

        return word_counts.most_common(1)[0][0]
        