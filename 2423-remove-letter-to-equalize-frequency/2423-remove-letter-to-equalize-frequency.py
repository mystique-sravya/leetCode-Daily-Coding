class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        """
        (Reduce TC from O(n2) -> O(n)

Instead of checking length of set elements everytime just check when it should be i.e., keep checking the freq of each char by removing 1 from it and also if it is zero.
        """
        counter = Counter(word)
        for c in word:
            counter[c] -= 1
            
            if counter[c] == 0:
                counter.pop(c)
            
            if len(set(counter.values())) == 1:
                return True

            counter[c] += 1
        return False