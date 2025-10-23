from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for punc in ["!", "?", "'", ",", ";", "."]:
            paragraph = paragraph.replace(punc, " ")
        words = [word.lower() for word in paragraph.split()]
        print(words)

        word_counts = Counter(words)
        banned = set(banned)

        top_words = sorted(list(word_counts.keys()), key = lambda x: word_counts[x], reverse = True)

        for top_word in top_words:
            if top_word not in banned:
                return top_word

        