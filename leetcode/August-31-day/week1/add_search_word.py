"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""
import re
class WordDictionary:

    def __init__(self):
        self.words = "#"
        

    def addWord(self, word: str) -> None:
        self.words += word+"#"
        

    def search(self, word: str) -> bool:
        return bool(re.search('#' + word + '#', self.words))
        