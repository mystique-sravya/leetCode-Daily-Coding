class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        char_count = Counter()
        
        for word in words:
            char_count.update(word)
        
        for count in char_count.values():
            if count % length != 0:
                return False
        
        return True