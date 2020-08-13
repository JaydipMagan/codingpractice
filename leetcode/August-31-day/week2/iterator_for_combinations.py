"""
Design an Iterator class, which has:

    A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    A function next() that returns the next combination of length combinationLength in lexicographical order.
    A function hasNext() that returns True if and only if there exists a next combination.

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false

Constraints:

    1 <= combinationLength <= characters.length <= 15
    There will be at most 10^4 function calls per test.
    It's guaranteed that all calls of the function next are valid.
"""
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.chars_len = len(characters)
        self.combinations = self.get_comb(combinationLength,self.chars_len)
        self.index = len(self.combinations)-1

    def next(self) -> str:
        res = ""
        for i in range(self.chars_len):
            if self.combinations[self.index][i]!="0":
                res+=self.characters[i]
        self.index-=1
        return res

    def hasNext(self) -> bool:
        return self.index>-1

    def get_comb(self,comb_len,chars_len):
        res = []
        for i in range(int(chars_len*"1",2)):
            b = bin(i)[2:]
            if b.count('1')==comb_len:
                res.append(b.zfill(chars_len))
        return res
                
            