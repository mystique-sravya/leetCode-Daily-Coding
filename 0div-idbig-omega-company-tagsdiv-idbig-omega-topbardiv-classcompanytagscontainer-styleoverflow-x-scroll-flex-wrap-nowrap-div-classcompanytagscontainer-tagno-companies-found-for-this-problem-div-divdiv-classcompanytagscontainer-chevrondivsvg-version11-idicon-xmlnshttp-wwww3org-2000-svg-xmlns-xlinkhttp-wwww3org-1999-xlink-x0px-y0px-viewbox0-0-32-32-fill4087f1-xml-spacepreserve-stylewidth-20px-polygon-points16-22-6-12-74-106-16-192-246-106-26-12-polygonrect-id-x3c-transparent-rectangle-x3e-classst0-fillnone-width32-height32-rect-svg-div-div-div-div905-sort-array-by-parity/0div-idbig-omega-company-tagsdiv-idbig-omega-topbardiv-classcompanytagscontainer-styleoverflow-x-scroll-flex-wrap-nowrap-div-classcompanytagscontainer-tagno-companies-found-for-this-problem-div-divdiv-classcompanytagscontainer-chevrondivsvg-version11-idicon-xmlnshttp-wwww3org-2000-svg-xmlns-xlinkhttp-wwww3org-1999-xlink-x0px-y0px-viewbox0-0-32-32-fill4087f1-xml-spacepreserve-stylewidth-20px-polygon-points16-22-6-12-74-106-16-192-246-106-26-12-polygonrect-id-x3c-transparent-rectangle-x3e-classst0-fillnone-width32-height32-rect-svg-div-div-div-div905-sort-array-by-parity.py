class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        eve = [i for i in nums if i %2 == 0]
        eve.sort()
        odd = [i for i in nums if i %2 != 0]
        odd.sort()
        m = eve + odd
        return m