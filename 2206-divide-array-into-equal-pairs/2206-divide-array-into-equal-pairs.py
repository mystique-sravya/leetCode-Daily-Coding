class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd = [False] * 501
        for n in nums:
            odd[n] = not odd[n]
        return not any(odd)