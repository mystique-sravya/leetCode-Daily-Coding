class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d, d2 = Counter(ransomNote), Counter(magazine)
        if d & d2 == d:
            return True
        return False