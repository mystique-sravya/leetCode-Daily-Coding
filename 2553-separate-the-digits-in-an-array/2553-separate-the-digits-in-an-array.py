class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = []
        for i in nums:
            s = str(i)
            for x in s:
                n.append(int(x))
        return n