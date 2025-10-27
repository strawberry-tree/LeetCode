class Node:
    def __init__(self, value):
        self.value = value
        self.end_of_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node("")    # sentinel node    

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                new_child = Node(letter)
                curr.children[letter] = new_child
                curr = curr.children[letter]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return curr.end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)