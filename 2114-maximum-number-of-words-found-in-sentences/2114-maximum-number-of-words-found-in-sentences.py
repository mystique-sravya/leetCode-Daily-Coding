class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxwords = 0
        for i in sentences:
            maxwords = max(maxwords,len(i.split(" ")))
        return maxwords