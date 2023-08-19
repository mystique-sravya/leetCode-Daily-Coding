class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpa = 'abcdefghijklmnopqrstuvwxyz'
        
        ls = len(set(sentence))
        if len(alpa) == ls:
            return True
        return False