class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            arr += [encoded[i]^arr[-1]]
        return arr
