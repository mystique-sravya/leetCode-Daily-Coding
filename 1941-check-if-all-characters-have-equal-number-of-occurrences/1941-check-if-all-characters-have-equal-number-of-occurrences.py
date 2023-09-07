class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i] = s.count(i)
        first_value = list(d.values())[0]
        all_equal = all(value == first_value for value in d.values())
        return all_equal